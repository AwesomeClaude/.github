/* The Nine Lives of Ash — standalone battle prototype, no dependencies. */
/* Prologue rules (authoritative: rules.json, skills.json, enemies.json,
   story/prologue/01_the_gift.json): Ash 10 HP, The Vole 5 HP, 3 paws per
   turn, opening hand exactly 3 Ferocity. Pounce 2 Fer/4 dmg/3 charges,
   Slink 1 Sha/3 Block/3 charges, Purr 1 Gui/2 charges (heal 2 per turn
    over 2 turns, seals skills and Concentrate, Slip Away stays open,
    broken by damage), Loaf 1 Gui/2 charges
   (5 Block, guards the hand, commits the turn), Scratch free once per
   turn for 1. The Vole telegraphs Hold Very Still (nothing) and
   Dart for Cover (takes 1 energy). Concentrate: 2 per fight, costs the
   whole turn, wills 1 spent energy back. Slip Away is free but the
   Vole gets its telegraphed move as a parting shot.
   Browser simplification: token energy counters stand in for the energy
   spool/hand; the +1 Ferocity draw per turn stands in for the slow-draw
   economy (the vole deck's tail is all Ferocity); one Concentrate button
   recovers the most-spent humour. Not exact card parity. */
"use strict";

var $ = function (id) { return document.getElementById(id); };

var INTENTS = [
  { k: "still", name: "Hold Very Still" },
  { k: "dart", name: "Dart for Cover" }
];

var S = {
  lives: 9,
  turn: 1,
  paws: 3,
  over: false,
  php: 10,
  pmax: 10,
  pblk: 0,
  ehp: 5,
  emax: 5,
  eblk: 0,
  en: { fer: 3, gui: 0, sha: 0 },
  spent: { fer: 0, gui: 0, sha: 0 },
  concentrateLeft: 2,
  loafed: 0,
  intent: null,
  intentIndex: 0,
  scratchUsed: false,
  purrTurns: 0,
  charges: { pounce: 3, slink: 3, purr: 2, loaf: 2 }
};

function resetCharges() {
  S.charges = { pounce: 3, slink: 3, purr: 2, loaf: 2 };
}

function resetEnergies() {
  S.en = { fer: 3, gui: 0, sha: 0 };
  S.spent = { fer: 0, gui: 0, sha: 0 };
}

var CARDS = [
  {
    id: "scratch",
    name: "Scratch",
    cost: { paws: 0 },
    desc: "Instinct — free, once per turn: Deal 1 damage.",
    run: function () { S.scratchUsed = true; hitEnemy(1); }
  },
  {
    id: "pounce",
    name: "Pounce",
    cost: { paws: 1, fer: 2 },
    desc: "Deal 4 damage. 3 charges.",
    run: function () { S.charges.pounce -= 1; hitEnemy(4); }
  },
  {
    id: "slink",
    name: "Slink",
    cost: { paws: 1, sha: 1 },
    desc: "Gain 3 Block. 3 charges.",
    run: function () { S.charges.slink -= 1; gainBlock("p", 3); }
  },
  {
    id: "purr",
    name: "Purr",
    cost: { paws: 1, gui: 1 },
    desc: "Heal 2 per turn over 2 turns. Skills and Concentrate refused while channeling; Slip Away stays open; damage breaks it. 2 charges.",
    run: function () {
      S.charges.purr -= 1;
      S.purrTurns = 2;
      log("Ash begins purring — 2 HP per turn over 2 turns; skills sealed.");
    }
  },
  {
    id: "loaf",
    name: "Loaf",
    cost: { paws: 1, gui: 1 },
    desc: "Gain 5 Block, guard the hand, and end the turn. 2 charges.",
    run: function () {
      S.charges.loaf -= 1;
      S.loafed = 1;
      gainBlock("p", 5);
      log("Ash loafs — paws folded, nothing loose to take.");
    }
  }
];

function show(id) {
  var screens = ["screen-title", "screen-battle", "screen-end"];
  for (var i = 0; i < screens.length; i++) {
    $(screens[i]).classList.toggle("active", screens[i] === id);
  }
}

function log(m) {
  var el = $("log");
  var d = document.createElement("div");
  d.textContent = m;
  el.prepend(d);
  while (el.children.length > 40) el.lastChild.remove();
}

function hearts(n, max) {
  var s = "";
  for (var i = 0; i < max; i++) s += i < n ? "🧡" : "🤍";
  return s;
}

function channeling() {
  return S.purrTurns > 0;
}

function render() {
  $("player-hp-fill").style.width = Math.max(0, (S.php / S.pmax) * 100) + "%";
  $("player-hp-text").textContent = Math.max(0, S.php) + " / " + S.pmax;
  $("enemy-hp-fill").style.width = Math.max(0, (S.ehp / S.emax) * 100) + "%";
  $("enemy-hp-text").textContent = Math.max(0, S.ehp) + " / " + S.emax;
  $("player-block").textContent = "🛡 " + S.pblk;
  $("enemy-block").textContent = "🛡 " + S.eblk;
  $("en-fer").textContent = S.en.fer;
  $("en-gui").textContent = S.en.gui;
  $("en-sha").textContent = S.en.sha;

  var paws = $("paws");
  paws.innerHTML = "";
  for (var i = 0; i < 3; i++) {
    var s = document.createElement("span");
    s.textContent = "🐾";
    if (i >= S.paws) s.className = "spent";
    paws.appendChild(s);
  }

  var note = "";
  if (channeling()) note += " (purring: " + S.purrTurns + " left)";
  if (S.loafed > 0) note += " (loafed)";
  if (!S.scratchUsed) note += " — Scratch ready";
  $("turn-label").textContent = "Turn " + S.turn + " — your prowl" + note +
    " — Concentrate ×" + S.concentrateLeft;
  $("lives-mini").textContent = "🧡×" + S.lives;
  $("title-lives").textContent = hearts(S.lives, 9);
  renderCards();
  renderIntent();
}

function costText(c) {
  var p = [];
  if (!c.paws) p.push("free");
  else p.push(c.paws + " 🐾");
  if (c.fer) p.push(c.fer + " Fer");
  if (c.gui) p.push(c.gui + " Gui");
  if (c.sha) p.push(c.sha + " Sha");
  return p.join(" + ");
}

function skillsSealed() {
  return channeling() || S.loafed > 0;
}

function cardDisabled(c) {
  if (S.over) return true;
  if (skillsSealed()) return true;
  if (c.id === "scratch" && S.scratchUsed) return true;
  if (c.id !== "scratch" && S.charges[c.id] <= 0) return true;
  return !canPay(c.cost);
}

function canPay(c) {
  return (
    S.paws >= (c.paws || 0) &&
    S.en.fer >= (c.fer || 0) &&
    S.en.gui >= (c.gui || 0) &&
    S.en.sha >= (c.sha || 0)
  );
}

function pay(c) {
  S.paws -= c.paws || 0;
  if (c.fer) { S.en.fer -= c.fer; S.spent.fer += c.fer; }
  if (c.gui) { S.en.gui -= c.gui; S.spent.gui += c.gui; }
  if (c.sha) { S.en.sha -= c.sha; S.spent.sha += c.sha; }
}

function chargesText(c) {
  if (c.id === "scratch") return S.scratchUsed ? "used" : "ready";
  return "×" + S.charges[c.id];
}

function spentTotal() {
  return S.spent.fer + S.spent.gui + S.spent.sha;
}

function renderCards() {
  var w = $("cards");
  w.innerHTML = "";
  CARDS.forEach(function (c, i) {
    var b = document.createElement("button");
    b.className = "card";
    b.disabled = cardDisabled(c);
    b.setAttribute("aria-label", c.name + " (" + costText(c.cost) + ", " + chargesText(c) + ")");
    if (skillsSealed()) b.classList.add("sealed");

    var t = document.createElement("span");
    t.className = "t";
    t.textContent = c.name + " " + chargesText(c);
    var k = document.createElement("span");
    k.className = "key";
    k.textContent = String(i + 1);
    t.appendChild(k);

    var cc = document.createElement("span");
    cc.className = "c";
    cc.textContent = costText(c.cost);

    var d = document.createElement("span");
    d.className = "d";
    d.textContent = c.desc;

    b.append(t, cc, d);
    b.onclick = function () { playCard(i); };
    w.appendChild(b);
  });
  var sealed = S.over || skillsSealed();
  $("btn-concentrate").disabled = sealed || S.concentrateLeft <= 0 || spentTotal() <= 0;
  $("btn-slip").disabled = S.over;
  $("btn-end").disabled = S.over;
}

function renderIntent() {
  var ic = $("intent-icon");
  var tx = $("intent-text");
  if (!S.intent) {
    ic.textContent = "❓";
    tx.textContent = "The Vole sniffs the air…";
    return;
  }
  if (S.intent.k === "dart") {
    ic.textContent = "🌀";
    tx.textContent = "The Vole plans Dart for Cover — it will take 1 energy (Loaf guards).";
  } else {
    ic.textContent = "🐭";
    tx.textContent = "The Vole plans to Hold Very Still — nothing incoming.";
  }
}

function flash(enemy) {
  var el = enemy ? $("enemy-card") : document.querySelector(".fighter.player");
  if (!el) return;
  el.classList.remove("flash");
  void el.offsetWidth;
  el.classList.add("flash");
}

function dmg(target, v) {
  if (target === "p") {
    var b = Math.min(S.pblk, v);
    S.pblk -= b;
    var lost = v - b;
    S.php -= lost;
    if (lost > 0 && channeling()) {
      S.purrTurns = 0;
      log("The purr breaks.");
    }
  } else {
    var eb = Math.min(S.eblk, v);
    S.eblk -= eb;
    S.ehp -= v - eb;
  }
  flash(target === "e");
}

function hitEnemy(v) {
  dmg("e", v);
  log("Ash deals " + v + " to The Vole.");
}

function gainBlock(who, v) {
  if (who === "p") S.pblk += v;
  else S.eblk += v;
  log((who === "p" ? "Ash" : "The Vole") + " gains " + v + " Block.");
}

function heal(v) {
  S.php = Math.min(S.pmax, S.php + v);
  log("Ash recovers " + v + " HP.");
}

function rollIntent() {
  S.intent = INTENTS[S.intentIndex % INTENTS.length];
  S.intentIndex += 1;
}

var HUMOUR_NAMES = { fer: "Ferocity", gui: "Guile", sha: "Shadow" };

function stealEnergy() {
  if (S.loafed > 0) {
    log("The Vole finds nothing loose to take — Ash is loafed.");
    return;
  }
  var avail = [];
  if (S.en.fer > 0) avail.push("fer");
  if (S.en.gui > 0) avail.push("gui");
  if (S.en.sha > 0) avail.push("sha");
  if (avail.length === 0) {
    log("The Vole darts for cover — empty paws, nothing to take.");
    return;
  }
  var h = avail[Math.floor(Math.random() * avail.length)];
  S.en[h] -= 1;
  S.spent[h] += 1;
  log("The Vole darts for cover — takes 1 " + HUMOUR_NAMES[h] + ".");
}

function enemyAct() {
  var it = S.intent;
  if (!it) return;
  if (it.k === "dart") {
    stealEnergy();
  } else {
    log("The Vole holds very still. It believes this is working.");
  }
}

function playCard(i) {
  if (S.over) return;
  if (channeling()) {
    log("The purr holds him still — skills and Concentrate refused; Slip Away stays open.");
    return;
  }
  if (S.loafed > 0) {
    log("Loafed: all paws are committed.");
    return;
  }
  var c = CARDS[i];
  if (!c) return;
  if (c.id === "scratch" && S.scratchUsed) {
    log("Scratch is once per turn.");
    return;
  }
  if (c.id !== "scratch" && S.charges[c.id] <= 0) {
    log(c.name + " has no charges left.");
    return;
  }
  if (!canPay(c.cost)) {
    log("Not enough paws/energy for " + c.name + ".");
    return;
  }
  pay(c.cost);
  c.run();
  var loaf = c.id === "loaf";
  render();
  if (checkEnd()) return;
  if (loaf) endTurn();
}

function newTurn() {
  S.turn += 1;
  S.paws = 3;
  S.pblk = 0;
  S.loafed = 0;
  S.scratchUsed = false;
  if (S.purrTurns > 0) {
    S.purrTurns -= 1;
    heal(2);
    if (S.purrTurns === 0) log("The purr finishes, warm.");
  }
  S.en.fer = Math.min(9, S.en.fer + 1);
  rollIntent();
  render();
}

function endTurn() {
  if (S.over) return;
  enemyAct();
  render();
  if (checkEnd()) return;
  newTurn();
  log("— Turn " + S.turn + " — Ash draws a Ferocity.");
}

function checkEnd() {
  if (S.ehp <= 0) {
    win(false);
    return true;
  }
  if (S.php <= 0) {
    S.lives -= 1;
    if (S.lives <= 0) {
      lose();
    } else {
      S.php = S.pmax;
      S.ehp = S.emax;
      S.pblk = 0;
      S.eblk = 0;
      S.purrTurns = 0;
      S.loafed = 0;
      S.scratchUsed = false;
      S.concentrateLeft = 2;
      S.intentIndex = 0;
      resetCharges();
      resetEnergies();
      rollIntent();
      log("Ash loses a life! " + S.lives + " remain — the fight restarts.");
      render();
    }
    render();
    return S.lives <= 0;
  }
  return false;
}

function endScreen(kicker, title, art, text) {
  S.over = true;
  $("end-kicker").textContent = kicker;
  $("end-title").textContent = title;
  $("end-art").textContent = art;
  $("end-text").textContent = text;
  $("end-lives").textContent = hearts(S.lives, 9);
  show("screen-end");
  renderCards();
}

function win(slip) {
  endScreen(
    "The tale pauses",
    slip ? "Clean Escape" : "Victory",
    slip ? "🌫️" : "🌙",
    slip
      ? "Ash slips away unharmed into the shadows."
      : "The Vole flees! Ash keeps " + S.lives + " of nine lives."
  );
  log(slip ? "Ash slipped away." : "Victory!");
}

function lose() {
  S.lives = 0;
  endScreen(
    "The tale ends",
    "All Nine Lives Spent",
    "🥀",
    "The Vole stands over the storybook. Try again?"
  );
}

function startBattle() {
  S.turn = 1;
  S.paws = 3;
  S.over = false;
  S.php = S.pmax;
  S.pblk = 0;
  S.ehp = S.emax;
  S.eblk = 0;
  S.intent = null;
  S.intentIndex = 0;
  S.scratchUsed = false;
  S.purrTurns = 0;
  S.loafed = 0;
  S.concentrateLeft = 2;
  resetCharges();
  resetEnergies();
  rollIntent();
  $("log").innerHTML = "";
  show("screen-battle");
  log("Battle begins: Ash (10 HP) vs The Vole (5 HP). Open: 3 Ferocity.");
  render();
}

function bestSpentHumour() {
  var order = ["sha", "gui", "fer"];
  var best = null;
  var bestN = 0;
  for (var i = 0; i < order.length; i++) {
    var h = order[i];
    if (S.spent[h] > bestN) {
      best = h;
      bestN = S.spent[h];
    }
  }
  return best;
}

function init() {
  $("btn-start").onclick = startBattle;
  $("btn-again").onclick = function () {
    if (S.lives <= 0) S.lives = 9;
    startBattle();
  };
  $("btn-title").onclick = function () {
    S.over = true;
    show("screen-title");
    render();
  };
  $("btn-quit").onclick = function () {
    show("screen-title");
    render();
  };
  $("btn-restart").onclick = startBattle;
  $("btn-end").onclick = endTurn;

  $("btn-how").onclick = function () {
    var h = $("howto");
    var open = h.hidden;
    h.hidden = !open;
    $("btn-how").setAttribute("aria-expanded", String(open));
  };

  $("btn-concentrate").onclick = function () {
    if (channeling()) {
      log("The purr holds him still — skills and Concentrate refused; Slip Away stays open.");
      return;
    }
    if (S.over || skillsSealed() || S.concentrateLeft <= 0) return;
    var h = bestSpentHumour();
    if (!h) {
      log("No spent energy to will back.");
      return;
    }
    S.spent[h] -= 1;
    S.en[h] = Math.min(9, S.en[h] + 1);
    S.concentrateLeft -= 1;
    log("Ash concentrates: wills 1 " + HUMOUR_NAMES[h] + " back (" + S.concentrateLeft + " left).");
    render();
    endTurn();
  };

  $("btn-slip").onclick = function () {
    if (S.over) return;
    log("Ash turns to slip away — the Vole gets a parting shot.");
    enemyAct();
    render();
    if (checkEnd()) return;
    win(true);
  };

  document.addEventListener("keydown", function (e) {
    if (!$("screen-battle").classList.contains("active") || S.over) return;
    if (e.key >= "1" && e.key <= "5") playCard(Number(e.key) - 1);
    else if (e.key === "e" || e.key === "E") endTurn();
  });

  render();
}

document.addEventListener("DOMContentLoaded", init);
