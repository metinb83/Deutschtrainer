from flask import Flask, render_template

app = Flask(__name__)

# --- 1) Artikelregeln data ---
artikel_data = """
der Tourismus, der Kapitalismus, der Kommunismus, der Nationalismus, der Realismus,
der Idealismus, der Pessimismus, der Optimismus, der Egoismus, der Tourist,
der Journalist, der Aktivist, der Polizist, der Zivilist, der Motor, der Doktor,
der Autor, der Direktor, der Faktor, der Monitor, der Arzt, der Pilot, der Lehrer,
die Ordnung, die Bewegung, die Erfahrung, die Bedeutung, die Leistung, die Erinnerung,
die Entdeckung, die Lösung, die Verbindung, die Entwicklung, die Erhöhung,
die Entscheidung, die Bedingung, die Freiheit, die Gesundheit, die Sicherheit,
die Schwierigkeit, die Möglichkeit, die Wahrheit, die Öffentlichkeit, die Klarheit,
die Menschheit, die Dankbarkeit, die Traurigkeit, die Sauberkeit, die Freundlichkeit,
die Ewigkeit, die Wirklichkeit, die Einsamkeit, die Nation, die Diskussion,
die Tradition, die Religion, die Reaktion, die Produktion, die Position,
die Situation, die Konstruktion, die Revolution, die Option, die Intuition,
die Aktion, die Universität, die Qualität, die Kreativität, die Aktivität,
die Realität, die Identität, die Stabilität, die Toleranz, die Frequenz,
die Konferenz, die Konkurrenz, die Intelligenz, die Musik, die Technik,
die Politik, die Elektronik, die Klinik, die Optik, die Logik, die Ethik,
die Grammatik, die Physik, die Statistik, die Kritik, die Mechanik,
die Bäckerei, die Metzgerei, die Bücherei, die Gärtnerei, die Polizei,
die Blume, die Lampe, die Welle, die Katze, die Brücke, die Straße,
die Schule, die Flasche, die Kerze, die Sprache, die Zunge, das Mädchen,
das Brötchen, das Häuschen, das Bäumchen, das Kätzchen, das Hündchen,
das Blümchen, das Gläschen, das Dokument, das Instrument, das Argument,
das Experiment, das Element, das Parlament, das Kompliment, das Fundament,
das Medikament, das Datum, das Zentrum, das Museum, das Maximum, das Minimum,
das Album, das Forum, das Spektrum, das Ereignis, das Zeugnis, das Ergebnis,
das Verhältnis, das Verständnis, das Geheimnis, das Gefängnis, das Gedächtnis,
das Thema, das Schema, das Drama, das Aroma, das Klima, das Trauma,
das Dilemma, das Charisma, das Stigma, der Komponist, der Generator,
der Moderator, der Projektor, der Mentor
""".strip()

words = []
for item in artikel_data.split(","):
    parts = item.strip().split(" ", 1)
    if len(parts) == 2:
        article, noun = parts
        words.append({"article": article, "noun": noun})

# --- 2) Gegenteile (Adjektive) data ---
adj_data = """
laut, leise
schwierig, einfach
schnell, langsam
schwer, leicht
groß, klein
offen, geschlossen
alt, jung
teuer, billig
heiß, kalt
trocken, nass
scharf, mild
optimistisch, pessimistisch
gesund, krank
sauber, schmutzig
faul, fleißig
hell, dunkel
gut, schlecht
früh, spät
viel, wenig
richtig, falsch
schön, hässlich
lang, kurz
voll, leer
warm, kühl
spannend, langweilig
hart, weich
reich, arm
hungrig, satt
ruhig, nervös
modern, altmodisch
stark, schwach
""".strip()

adj_pairs = []
for line in adj_data.splitlines():
    a, b = line.split(",", 1)
    adj_pairs.append({"a": a.strip(), "b": b.strip()})

# --- 3) Gegenteile (Verben) data ---
verb_data = """
kommen, gehen
geben, nehmen
gewinnen, verlieren
suchen, finden
kaufen, verkaufen
aufmachen, zumachen
öffnen, schließen
aufschließen, abschließen
anmachen, ausmachen
anschalten, ausschalten
verbessern, verschlechtern
anfangen, aufhören
beginnen, beenden
fragen, antworten
behalten, entsorgen
erhöhen, reduzieren
steigen, sinken
reingehen, rausgehen
hochgehen, runtergehen
lieben, hassen
akzeptieren, ablehnen
betreten, verlassen
Geld ausgeben, Geld sparen
einschlafen, aufwachen
reparieren, kaputtmachen
""".strip()

verb_pairs = []
for line in verb_data.splitlines():
    a, b = line.split(",", 1)
    verb_pairs.append({"a": a.strip(), "b": b.strip()})

# --- 4) Verben und Fall data ---
case_data = """
Ich sehe, akk
Ich brauche, akk
Ich treffe, akk
Ich suche, akk
Ich kenne, akk
Ich höre, akk
Ich verstehe, akk
Ich frage, akk
Ich besuche, akk
Ich liebe, akk
Ich mag, akk
Ich beobachte, akk
Das Buch ist für, akk
Ich helfe, dat
Ich folge, dat
Ich glaube, dat
Ich danke, dat
Ich antworte, dat
Ich gebe, dat
Ich zeige, dat
Ich bringe, dat
Ich erzähle, dat
Ich schicke, dat
Ich empfehle, dat
Ich stehe bei, dat
Ich spreche mit, dat
Ich gehe zu, dat
Das Buch gehört, dat
Das Buch gefällt, dat
""".strip()

case_pairs = []
for line in case_data.splitlines():
    phrase, case = line.split(",", 1)
    case_pairs.append({"phrase": phrase.strip(), "case": case.strip()})

# --- 5) Personalpronomen 3. Person Singular data ---
personal_data = """
Ich sehe, den Mann, ihn
Ich sehe, den Plan, ihn
Ich sehe, den Weg, ihn
Ich sehe, Peter, ihn
Ich sehe, Markus, ihn
Ich sehe, Ali, ihn
Ich sehe, das Kind, es
Ich sehe, das Auto, es
Ich sehe, das Schild, es
Ich sehe, das Problem, es
Ich sehe, das Flugzeug, es
Ich sehe, die Frau, sie
Ich sehe, die Straße, sie
Ich sehe, die Karte, sie
Ich sehe, Maria, sie
Ich sehe, Anna, sie
Ich sehe, Lisa, sie
Ich frage, den Chef, ihn
Ich frage, den Lehrer, ihn
Ich frage, den Polizist, ihn
Ich frage, Peter, ihn
Ich frage, das Kind, es
Ich frage, die Chefin, sie
Ich frage, die Lehrerin, sie
Ich frage, die Polizistin, sie
Ich frage, Maria, sie
Ich folge, dem Mann, ihm
Ich folge, dem Plan, ihm
Ich folge, dem Weg, ihm
Ich folge, Peter, ihm
Ich folge, Markus, ihm
Ich folge, Ali, ihm
Ich folge, dem Kind, ihm
Ich folge, dem Auto, ihm
Ich folge, dem Schild, ihm
Ich folge, der Frau, ihr
Ich folge, der Straße, ihr
Ich folge, der Karte, ihr
Ich folge, Maria, ihr
Ich folge, Anna, ihr
Ich folge, Lisa, ihr
Ich helfe, dem Mann, ihm
Ich helfe, dem Lehrer, ihm
Ich helfe, Peter, ihm
Ich helfe, dem Kind, ihm
Ich helfe, der Frau, ihr
Ich helfe, der Lehrerin, ihr
Ich helfe, Maria, ihr
""".strip()

personal_pairs = []
for line in personal_data.splitlines():
    phrase, continuation, pronoun = line.split(",", 2)
    personal_pairs.append({
        "phrase": phrase.strip(),
        "continuation": continuation.strip(),
        "pronoun": pronoun.strip()
    })

# --- 6) Modalverben data ---
modal_data = """
Ich koche sehr oft. Ich, kann, gut kochen.
Du kochst sehr oft. Du, kannst, gut kochen.
Tom kocht sehr oft. Er, kann, gut kochen.
Lisa kocht sehr oft. Sie, kann, gut kochen.
Wir kochen sehr oft. Wir, können, gut kochen.
Ihr kocht sehr oft. Ihr, könnt, gut kochen.
Tom und Lisa kochen sehr oft. Sie, können, gut kochen.
Das Paket ist nicht schwer. Ich, kann, das Paket tragen.
Das Paket ist nicht schwer. Du, kannst, das Paket tragen.
Das Paket ist nicht schwer. Tom, kann, das Paket tragen.
Das Paket ist nicht schwer. Lisa, kann, das Paket tragen.
Das Paket ist nicht schwer. Wir, können, das Paket tragen.
Das Paket ist nicht schwer. Ihr, könnt, das Paket tragen.
Das Paket ist nicht schwer. Tom und Lisa, können, das Paket tragen.
Ich kenne die Regeln von Monopoly. Ich, kann, Monopoly spielen.
Du kennst die Regeln von Monopoly. Du, kannst, Monopoly spielen.
Tom kennt die Regeln von Monopoly. Er, kann, Monopoly spielen.
Lisa kennt die Regeln von Monopoly. Sie, kann, Monopoly spielen.
Wir kennen die Regeln von Monopoly. Wir, können, Monopoly spielen.
Ihr kennt die Regeln von Monopoly. Ihr, könnt, Monopoly spielen.
Tom und Lisa kennen die Regeln von Monopoly. Sie, können, Monopoly spielen.
Ich bin krank. Ich, kann, heute nicht arbeiten.
Du bist krank. Du, kannst, heute nicht arbeiten.
Tom ist krank. Er, kann, heute nicht arbeiten.
Lisa ist krank. Sie, kann, heute nicht arbeiten.
Wir sind krank. Wir, können, heute nicht arbeiten.
Ihr seid krank. Ihr, könnt, heute nicht arbeiten.
Tom und Lisa sind krank. Sie, können, heute nicht arbeiten.
Alles ist bereit. Ich, kann, jetzt beginnen.
Alles ist bereit. Du, kannst, jetzt beginnen.
Alles ist bereit. Tom, kann, jetzt beginnen.
Alles ist bereit. Lisa, kann, jetzt beginnen.
Alles ist bereit. Wir, können, jetzt beginnen.
Alles ist bereit. Ihr, könnt, jetzt beginnen.
Alles ist bereit. Tom und Lisa, können, jetzt beginnen.
Die Musik ist laut. Ich, muss, lauter sprechen.
Die Musik ist laut. Du, musst, lauter sprechen.
Die Musik ist laut. Tom, muss, lauter sprechen.
Die Musik ist laut. Lisa, muss, lauter sprechen.
Die Musik ist laut. Wir, müssen, lauter sprechen.
Die Musik ist laut. Ihr, müsst, lauter sprechen.
Die Musik ist laut. Tom und Lisa, müssen, lauter sprechen.
Ich habe morgen keine Zeit. Ich, muss, morgen arbeiten.
Du hast morgen keine Zeit. Du, musst, morgen arbeiten.
Tom hat morgen keine Zeit. Er, muss, morgen arbeiten.
Lisa hat morgen keine Zeit. Sie, muss, morgen arbeiten.
Wir haben morgen keine Zeit. Wir, müssen, morgen arbeiten.
Ihr habt morgen keine Zeit. Ihr, müsst, morgen arbeiten.
Tom und Lisa haben morgen keine Zeit. Sie, müssen, morgen arbeiten.
Der Zug kommt gleich. Ich, muss, jetzt gehen.
Der Zug kommt gleich. Du, musst, jetzt gehen.
Der Zug kommt gleich. Tom, muss, jetzt gehen.
Der Zug kommt gleich. Lisa, muss, jetzt gehen.
Der Zug kommt gleich. Wir, müssen, jetzt gehen.
Der Zug kommt gleich. Ihr, müsst, jetzt gehen.
Der Zug kommt gleich. Tom und Lisa, müssen, jetzt gehen.
Der Benzintank ist voll. Ich, muss, nicht tanken.
Der Benzintank ist voll. Du, musst, nicht tanken.
Der Benzintank ist voll. Tom, muss, nicht tanken.
Der Benzintank ist voll. Lisa, muss, nicht tanken.
Der Benzintank ist voll. Wir, müssen, nicht tanken.
Der Benzintank ist voll. Ihr, müsst, nicht tanken.
Der Benzintank ist voll. Tom und Lisa, müssen, nicht tanken.
Das Paket kommt morgen. Ich, muss, ein bisschen länger warten.
Das Paket kommt morgen. Du, musst, ein bisschen länger warten.
Das Paket kommt morgen. Tom, muss, ein bisschen länger warten.
Das Paket kommt morgen. Lisa, muss, ein bisschen länger warten.
Das Paket kommt morgen. Wir, müssen, ein bisschen länger warten.
Das Paket kommt morgen. Ihr, müsst, ein bisschen länger warten.
Das Paket kommt morgen. Tom und Lisa, müssen, ein bisschen länger warten.
Das ist kein Parkplatz. Ich, darf, hier nicht parken.
Das ist kein Parkplatz. Du, darfst, hier nicht parken.
Das ist kein Parkplatz. Tom, darf, hier nicht parken.
Das ist kein Parkplatz. Lisa, darf, hier nicht parken.
Das ist kein Parkplatz. Wir, dürfen, hier nicht parken.
Das ist kein Parkplatz. Ihr, dürft, hier nicht parken.
Das ist kein Parkplatz. Tom und Lisa, dürfen, hier nicht parken.
Das ist eine Raucher-Bar. Ich, darf, hier rauchen.
Das ist eine Raucher-Bar. Du, darfst, hier rauchen.
Das ist eine Raucher-Bar. Tom, darf, hier rauchen.
Das ist eine Raucher-Bar. Lisa, darf, hier rauchen.
Das ist eine Raucher-Bar. Wir, dürfen, hier rauchen.
Das ist eine Raucher-Bar. Ihr, dürft, hier rauchen.
Das ist eine Raucher-Bar. Tom und Lisa, dürfen, hier rauchen.
Das ist ein privater Garten. Ich, darf, hier nicht laufen.
Das ist ein privater Garten. Du, darfst, hier nicht laufen.
Das ist ein privater Garten. Tom, darf, hier nicht laufen.
Das ist ein privater Garten. Lisa, darf, hier nicht laufen.
Das ist ein privater Garten. Wir, dürfen, hier nicht laufen.
Das ist ein privater Garten. Ihr, dürft, hier nicht laufen.
Das ist ein privater Garten. Tom und Lisa, dürfen, hier nicht laufen.
Der Kopierer ist nur für Mitarbeiter. Ich, darf, ihn nicht benutzen.
Der Kopierer ist nur für Mitarbeiter. Du, darfst, ihn nicht benutzen.
Der Kopierer ist nur für Mitarbeiter. Tom, darf, ihn nicht benutzen.
Der Kopierer ist nur für Mitarbeiter. Lisa, darf, ihn nicht benutzen.
Der Kopierer ist nur für Mitarbeiter. Wir, dürfen, ihn nicht benutzen.
Der Kopierer ist nur für Mitarbeiter. Ihr, dürft, ihn nicht benutzen.
Der Kopierer ist nur für Mitarbeiter. Tom und Lisa, dürfen, ihn nicht benutzen.
""".strip()

modal_pairs = []
for line in modal_data.splitlines():
    prefix, verb, suffix = line.split(",", 2)
    modal_pairs.append({
        "prefix": prefix.strip(),
        "verb": verb.strip(),
        "suffix": suffix.strip()
    })

# --- X) Steigerung (Adjektive) data ---
steigerung_data = """
laut, lauter
leise, leiser
schwierig, schwieriger
einfach, einfacher
schnell, schneller
langsam, langsamer
schwer, schwerer
leicht, leichter
groß, größer
klein, kleiner
alt, älter
jung, jünger
teuer, teuerer
billig, billiger
heiß, heißer
kalt, kälter
scharf, schärfer
mild, milder
sauber, sauberer
schmutzig, schmutziger
faul, fauler
fleißig, fleißiger
hell, heller
dunkel, dunkler
gut, besser
schlecht, schlechter
früh, früher
spät, später
schön, schöner
hässlich, hässlicher
lang, länger
kurz, kürzer
warm, wärmer
kühl, kühler
spannend, spannender
langweilig, langweiliger
hart, härter
weich, weicher
reich, reicher
arm, ärmer
stark, stärker
schwach, schwächer
""".strip()

steigerung_pairs = []
for line in steigerung_data.splitlines():
    adj, comp = line.split(",", 1)
    steigerung_pairs.append({
        "adj":  adj.strip(),
        "comp": comp.strip()
    })

# --- N) Perfektform data ---
perfekt_data = """
ich koche, ich habe gekocht
ich lasse, ich habe gelassen
ich gebe, ich habe gegeben
ich sehe, ich habe gesehen
ich finde, ich habe gefunden
ich tue, ich habe getan
ich erhalte, ich habe erhalten
ich bekomme, ich habe bekommen
ich zeige, ich habe gezeigt
ich bringe, ich habe gebracht
ich nehme, ich habe genommen
ich sage, ich habe gesagt
ich halte, ich habe gehalten
ich spiele, ich habe gespielt
ich stelle, ich habe gestellt
ich weiß, ich habe gewusst
ich helfe, ich habe geholfen
ich arbeite, ich habe gearbeitet
ich setze, ich habe gesetzt
ich benutze, ich habe benutzt
ich schaffe, ich habe geschafft
ich verlasse, ich habe verlassen
ich erreiche, ich habe erreicht
ich brauche, ich habe gebraucht
ich treffe, ich habe getroffen
ich lebe, ich habe gelebt
ich wohne, ich habe gewohnt
ich spreche, ich habe gesprochen
ich ziehe, ich habe gezogen
ich gewinne, ich habe gewonnen
ich erwarte, ich habe erwartet
ich mache, ich habe gemacht
ich trage, ich habe getragen
ich schaue, ich habe geschaut
ich warte, ich habe gewartet
ich entscheide, ich habe entschieden
ich schreibe, ich habe geschrieben
ich ändere, ich habe geändert
ich suche, ich habe gesucht
ich versuche, ich habe versucht
ich zahle, ich habe gezahlt
ich bezahle, ich habe bezahlt
ich kenne, ich habe gekannt
ich höre, ich habe gehört
ich feiere, ich habe gefeiert
ich beginne, ich habe begonnen
ich verstehe, ich habe verstanden
ich lese, ich habe gelesen
ich verliere, ich habe verloren
ich spare, ich habe gespart
ich melde, ich habe gemeldet
ich erkläre, ich habe erklärt
ich hoffe, ich habe gehofft
ich denke, ich habe gedacht
ich schaue, ich habe geschaut
ich lerne, ich habe gelernt
ich hole, ich habe geholt
ich vergesse, ich habe vergessen
ich schließe, ich habe geschlossen
ich frage, ich habe gefragt
ich besuche, ich habe besucht
ich schicke, ich habe geschickt
ich esse, ich habe gegessen
ich trinke, ich habe getrunken
ich rufe, ich habe gerufen
ich erzähle, ich habe erzählt
ich schlafe, ich habe geschlafen
ich bestelle, ich habe bestellt
ich komme, ich bin gekommen
ich stehe, ich bin gestanden
ich gehe, ich bin gegangen
ich bleibe, ich bin geblieben
ich liege, ich bin gelegen
ich fahre, ich bin gefahren
ich steige, ich bin gestiegen
ich laufe, ich bin gelaufen
ich falle, ich bin gefallen
ich sitze, ich bin gesessen
ich fliege, ich bin geflogen
ich folge, ich bin gefolgt
""".strip()

perfekt_pairs = []
for line in perfekt_data.splitlines():
    present, past = line.split(",", 1)
    perfekt_pairs.append({
        "present": present.strip(),
        "past":    past.strip()
    })

# --- Verbkonjugation data ---
konj_data = """
machen, mache, machst, macht, machen, macht, machen
kommen, komme, kommst, kommt, kommen, kommt, kommen
stehen, stehe, stehst, steht, stehen, steht, stehen
gehen, gehe, gehst, geht, gehen, geht, gehen
finden, finde, findest, findet, finden, findet, finden
bleiben, bleibe, bleibst, bleibt, bleiben, bleibt, bleiben
zeigen, zeige, zeigst, zeigt, zeigen, zeigt, zeigen
bringen, bringe, bringst, bringt, bringen, bringt, bringen
sagen, sage, sagst, sagt, sagen, sagt, sagen
liegen, liege, liegst, liegt, liegen, liegt, liegen
spielen, spiele, spielst, spielt, spielen, spielt, spielen
stellen, stelle, stellst, stellt, stellen, stellt, stellen
arbeiten, arbeite, arbeitest, arbeitet, arbeiten, arbeitet, arbeiten
setzen, setze, setzt, setzt, setzen, setzt, setzen
benutzen, benutze, benutzt, benutzt, benutzen, benutzt, benutzen
schaffen, schaffe, schaffst, schafft, schaffen, schafft, schaffen
brauchen, brauche, brauchst, braucht, brauchen, braucht, brauchen
leben, lebe, lebst, lebt, leben, lebt, leben
steigen, steige, steigst, steigt, steigen, steigt, steigen
ziehen, ziehe, ziehst, zieht, ziehen, zieht, ziehen
hören, höre, hörst, hört, hören, hört, hören
warten, warte, wartest, wartet, warten, wartet, warten
suchen, suche, suchst, sucht, suchen, sucht, suchen
zahlen, zahle, zahlst, zahlt, zahlen, zahlt, zahlen
melden, melde, meldest, meldet, melden, meldet, melden
sitzen, sitze, sitzt, sitzt, sitzen, sitzt, sitzen
schließen, schließe, schließt, schließt, schließen, schließt, schließen
genießen, genieße, genießt, genießt, genießen, genießt, genießen
lösen, löse, löst, löst, lösen, löst, lösen
beenden, beende, beendest, beendet, beenden, beendet, beenden
heißen, heiße, heißt, heißt, heißen, heißt, heißen
reisen, reise, reist, reist, reisen, reist, reisen
schätzen, schätze, schätzt, schätzt, schätzen, schätzt, schätzen
bitten, bitte, bittest, bittet, bitten, bittet, bitten
grüßen, grüße, grüßt, grüßt, grüßen, grüßt, grüßen
leiten, leite, leitest, leitet, leiten, leitet, leiten
reden, rede, redest, redet, reden, redet, reden
tanzen, tanze, tanzt, tanzt, tanzen, tanzt, tanzen
raten, rate, ratest, ratet, raten, ratet, raten
parken, parke, parkst, parkt, parken, parkt, parken
ändern, ändere, änderst, ändert, ändern, ändert, ändern
wandern, wandere, wanderst, wandert, wandern, wandert, wandern
ärgern, ärgere, ärgerst, ärgert, ärgern, ärgert, ärgern
zögern, zögere, zögerst, zögert, zögern, zögert, zögern
fordern, fordere, forderst, fordert, fordern, fordert, fordern
lernen, lerne, lernst, lernt, lernen, lernt, lernen
denken, denke, denkst, denkt, denken, denkt, denken
holen, hole, holst, holt, holen, holt, holen
legen, lege, legst, legt, legen, legt, legen
glauben, glaube, glaubst, glaubt, glauben, glaubt, glauben
""".strip()

konj_pairs = []
for line in konj_data.splitlines():
    parts = [p.strip() for p in line.split(",")]
    if len(parts) == 7:
        basic, ich, du, er, wir, ihr, sie = parts
        konj_pairs.append({
            "basic": basic,
            "ich": ich,
            "du": du,
            "er": er,
            "wir": wir,
            "ihr": ihr,
            "sie": sie
        })

# Verbkonjugation II data
konj2_data = """
werden, werde, wirst, wird, werden, werdet, werden, Vokalwechsel → i
haben, habe, hast, hat, haben, habt, haben, kein Tipp verfügbar
sein, bin, bist, ist, sind, seid, sind, kein Tipp verfügbar
können, kann, kannst, kann, können, könnt, können, Modalverb
müssen, muss, musst, muss, müssen, müsst, müssen, Modalverb
sollen, soll, sollst, soll, sollen, sollt, sollen, Modalverb
wollen, will, willst, will, wollen, wollt, wollen, Modalverb
lassen, lasse, lässt, lässt, lassen, lasst, lassen, Vokalwechsel → ä
geben, gebe, gibst, gibt, geben, gebt, geben, Vokalwechsel → i
sehen, sehe, siehst, sieht, sehen, seht, sehen, Vokalwechsel → ie
tun, tue, tust, tut, tun, tut, tun, kein Tipp verfügbar
erhalten, erhalte, erhälst, erhält, erhalten, erhaltet, erhalten, Vokalwechsel → ä
nehmen, nehme, nimmst, nimmt, nehmen, nehmt, nehmen, Vokalwechsel → i
halten, halte, hälst, hält, halten, haltet, halten, Vokalwechsel → ä
dürfen, darf, darfst, darf, dürfen, dürft, dürfen, Modalverb
wissen, weiß, weißt, weiß, wissen, wisst, wissen, kein Tipp verfügbar
helfen, helfe, hilfst, hilft, helfen, helft, helfen, Vokalwechsel → i
verlassen, verlasse, verlässt, verlässt, verlassen, verlasst, verlassen, Vokalwechsel → ä
fahren, fahre, fährst, fährt, fahren, fahrt, fahren, Vokalwechsel → ä
treffen, treffe, triffst, trifft, treffen, trefft, treffen, Vokalwechsel → i
sprechen, spreche, sprichst, spricht, sprechen, sprecht, sprechen, Vokalwechsel → i
laufen, laufe, läufst, läuft, laufen, lauft, laufen, Vokalwechsel → ä
tragen, trage, trägst, trägt, tragen, tragt, tragen, Vokalwechsel → ä
fallen, falle, fällst, fällt, fallen, fallt, fallen, Vokalwechsel → ä
lesen, lese, liest, liest, lesen, lest, lesen, Vokalwechsel → ie
möchten, möchte, möchtest, möchte, möchten, möchtet, möchten, Modalverb
vergessen, vergesse, vergisst, vergisst, vergessen, vergesst, vergessen, Vokalwechsel → i
essen, esse, isst, isst, essen, esst, essen, Vokalwechsel → i
laden, lade, lädst, lädt, laden, ladet, laden, Vokalwechsel → ä
empfehlen, empfehle, empfiehlst, empfiehlt, empfehlen, empfehlt, empfehlen, Vokalwechsel → ie
mögen, mag, magst, mag, mögen, mögt, mögen, kein Tipp verfügbar
fangen, fange, fängst, fängt, fangen, fangt, fangen, Vokalwechsel → ä
schlafen, schlafe, schläfst, schläft, schlafen, schlaft, schlafen, Vokalwechsel → ä
waschen, wasche, wäschst, wäscht, waschen, wascht, waschen, Vokalwechsel → ä
""".strip()

konj2_pairs = []
for line in konj2_data.splitlines():
    parts = [p.strip() for p in line.split(",", 7)]
    basic, ich, du, er, wir, ihr, sie, warning = parts
    konj2_pairs.append({
        "basic": basic,
        "ich": ich,
        "du": du,
        "er": er,
        "wir": wir,
        "ihr": ihr,
        "sie": sie,
        "warning": warning
    })

# --- Fragewörter data ---
fragen_data = """
wo, wohnst du? Ich wohne in Basel.
wo, arbeitest du? Ich arbeite bei Novartis.
wo, bist du? Ich bin im Büro.
wo, ist Peter? Peter ist zu Hause.
wo, ist dein Handy? Mein Handy ist auf dem Tisch.
wo, ist die Apotheke? In der Schillerstraße.
woher, kommst du? Ich komme aus Mexiko.
woher, kommt dein Chef? Er kommt aus China.
woher, hast du diese Info? Von Peter.
wohin, gehst du jetzt? Ich gehe nach Hause.
wohin, gehst du nach dem Kurs? Ich gehe zum Rewe.
wohin, fließt der Rhein? Nach Köln.
was, machst du? Ich schaue einen Film.
was, machst du am Samstag? Ich gehe nach Zürich.
was, isst du gerne? Ich esse gerne Pizza.
was, kochst du? Ich koche Lasagne.
was, ist dein Lieblingsfilm? Titanic.
was, sind deine Hobbies? Tanzen und Schwimmen.
wann, isst du Frühstück? Um 7 Uhr.
wann, beginnt deine Arbeit? Um 8 Uhr.
wann, öffnet der Supermarkt? Um 7 Uhr.
wann, gehst du ins Bett? Um 22 Uhr.
wann, gehst du in den Urlaub? Im Juli.
wann, ist das Konzert? Morgen um 20 Uhr.
seit wann, lernst du Deutsch? Seit 2 Jahren.
seit wann, wohnst du in Basel? Seit 5 Jahren.
seit wann, arbeitest du hier? Seit 8 Jahren.
seit wann, machst du Yoga? Seit 4 Monaten.
wer, ist dein Chef? Mein Chef ist Peter.
wer, ist dein Lehrer? Mein Lehrer ist Thomas.
wer, ist Kanzler von Deutschland? Friedrich Merz.
wer, ist das auf dem Foto? Das ist mein Vater.
wer, möchte ein Eis essen? Ich.
wie, heißt deine Mutter? Meine Mutter heißt Lisa.
wie, ist das Wetter? Das Wetter ist gut.
wie, lange dauert der Flug? Circa 4 Stunden.
wie, lange machst du Pause? 30 Minuten.
wie, viele Zimmer hat deine Wohnung? 3 Zimmer.
wie, oft trinkst du Alkohol? Ein Mal pro Woche.
wie, groß ist ein Virus? Circa 100 Nanometer.
welche, Farbe hat dein Handy? Mein Handy ist grau.
welche, Social Media App benutzt du? Instagram.
welche, Stadt findest du am schönsten? Barcelona.
welche, Podcasts hörst du? Ich höre Deutsche Welle.
welche, Jahreszeit findest du am schönsten? Sommer.
welche, Creme benutzt du? Ich benutze Nivea.
warum, hast du keine Zeit? Weil ich arbeiten muss.
warum, machst du Sport? Weil ich fit bleiben will.
warum, bist du zu Hause? Weil ich krank bin.
warum, bist du müde? Weil ich nicht gut schlafe.
warum, hast du ein Samsung? Weil es besser ist.
""".strip()

fragen_pairs = []
for line in fragen_data.splitlines():
    q, phrase = line.split(",", 1)
    fragen_pairs.append({"q": q.strip(), "phrase": phrase.strip()})

# --- 7) Trennbare Verben data ---
trennbar_data = """
anrufen, Ich, rufe, jetzt meine Mutter, an, .
anrufen, Ich, rufe, dich um 17 Uhr, an, .
anrufen, Peter, ruft, mich morgen, an, .
anrufen, Maria, ruft, morgen die Arztpraxis, an, .
anrufen, Wir, rufen, später nochmal, an, .
anrufen, Wann, rufst, du deine Mutter, an, ?
anrufen, Wann, rufen, Sie Frau Müller, an, ?
anrufen, Warum, rufst, mich schon heute, an, ?
anmachen, Ich, mache, jetzt das Licht, an, .
anmachen, Peter, macht, immer das Radio, an, .
anmachen, Maria, macht, jetzt den Film, an, .
anmachen, Wir, machen, sofort den Computer, an, .
anmachen, Warum, machst, du das Licht, an, ?
ausziehen, Ich, ziehe, die Jacke, aus, .
ausziehen, Peter, zieht, seinen Pullover, aus, .
ausziehen, Maria, zieht, die Schuhe, aus, .
ausziehen, Wir, ziehen, die Schuhe an der Tür, aus, .
ausziehen, Warum, ziehst, du die Jacke, aus, ?
aufstehen, Ich, stehe, um 7 Uhr, auf, .
aufstehen, Peter, steht, immer früh, auf, .
aufstehen, Maria, steht, immer zu spät, auf, .
aufstehen, Wir, stehen, gerne früh, auf, .
aufstehen, Wann, stehst, du normalerweise, auf, ?
aufstehen, Wann, stehen, Sie normalerweise, auf, ?
aufräumen, Ich, räume, jetzt mein Zimmer, auf, .
aufräumen, Ich, räume, morgen den Schreibtisch, auf, .
aufräumen, Peter, räumt, seinen Schreibtisch, auf, .
aufräumen, Maria, räumt, das Wohnzimmer, auf, .
aufräumen, Wir, räumen, das Zimmer morgen, auf, .
aufräumen, Wann, räumst, du dein Zimmer, auf, ?
aufräumen, Wer, räumt, jetzt das Zimmer, auf, ?
weitermachen, Ich, mache, in 10 Minuten, weiter, .
weitermachen, Peter, macht, nach dem Urlaub, weiter, .
weitermachen, Maria, macht, morgen früh, weiter, .
weitermachen, Wir, machen, nach der Pause, weiter, .
weitermachen, Wann, machst, du endlich, weiter, ?
abholen, Ich, hole, meine Mutter vom Flughafen, ab, .
abholen, Peter, holt, dich vom Bahnhof, ab, .
abholen, Maria, holt, gerade ihre Tochter, ab, .
abholen, Wir, holen, dich vom Flughafen, ab, .
abholen, Wann, holst, du mich, ab, ?
abholen, Wann, holen, Sie mich, ab, ?
abholen, Wer, holt, mich vom Bahnhof, ab, ?
mitbringen, Ich, bringe, das Buch, mit, .
mitbringen, Ich, bringe, Wasser und Cola, mit, .
mitbringen, Peter, bringt, den Grill, mit, .
mitbringen, Maria, bringt, das Ladekabel, mit, .
mitbringen, Wir, bringen, alle Dokumente, mit, .
mitbringen, Was, bringst, du zur Grillparty, mit, ?
zurückkommen, Ich, komme, am Montag, zurück, .
zurückkommen, Ich, komme, am 7. Juli, zurück, .
zurückkommen, Peter, kommt, morgen Abend, zurück, .
zurückkommen, Maria, kommt, nächste Woche, zurück, .
zurückkommen, Wir, kommen, heute Abend, zurück, .
zurückkommen, Wann, kommst, du vom Urlaub, zurück, ?
zurückkommen, Wann, kommen, Sie von der Reise, zurück, ?
ankommen, Ich, komme, um 17 Uhr, an, .
ankommen, Peter, kommt, morgen früh, an, .
ankommen, Maria, kommt, um 9 Uhr, an, .
ankommen, Wir, kommen, um circa 20 Uhr, an, .
ankommen, Wann, kommst, du am Flughafen, an, ?
ankommen, Um wie viel Uhr, kommen, Sie am Hotel, an, ?
ankommen, Warum, kommen, Sie so spät, an, ?
aufmachen, Es ist heiß. Ich, mache, das Fenster, auf, .
aufmachen, Ich habe Hunger. Ich, mache, die Chips, auf, .
aufmachen, Peter, macht, das Fenster, auf, .
""".strip()

trennbar_pairs = []
for line in trennbar_data.splitlines():
    infinitive, part2, answer1, part4, answer2, punct = [p.strip() for p in line.split(",", 5)]
    trennbar_pairs.append({
        "infinitive": infinitive,
        "part2":      part2,
        "answer1":    answer1,
        "part4":      part4,
        "answer2":    answer2,
        "punct":      punct
    })

# --- X) Sein-Konjugation data ---
sein_data = """
Ich, bin, in Basel.
Du, bist, in Basel.
Tom, ist, in Basel.
Maria, ist, in Basel.
Wir, sind, in Basel.
Ihr, seid, in Basel.
Tom und Maria, sind, in Basel.
Ich, bin, vor dem Restaurant.
Du, bist, vor dem Restaurant.
Tom, ist, vor dem Restaurant.
Maria, ist, vor dem Restaurant.
Wir, sind, vor dem Restaurant.
Ihr, seid, vor dem Restaurant.
Tom und Maria, sind, vor dem Restaurant.
Ich, bin, sehr freundlich.
Du, bist, sehr freundlich.
Tom, ist, sehr freundlich.
Maria, ist, sehr freundlich.
Wir, sind, sehr freundlich.
Ihr, seid, sehr freundlich.
Tom und Maria, sind, sehr freundlich.
Ich, bin, im Büro.
Du, bist, im Büro.
Tom, ist, im Büro.
Maria, ist, im Büro.
Wir, sind, im Büro.
Ihr, seid, im Büro.
Tom und Maria, sind, im Büro.
Ich, bin, Polizist von Beruf.
Du, bist, Polizist von Beruf.
Tom, ist, Polizist von Beruf.
Maria, ist, Polizist von Beruf.
Ihr, seid, Polizist von Beruf.
Tom und Maria, sind, Polizist von Beruf.
Ich, bin, 32 Jahre alt.
Du, bist, 32 Jahre alt.
Tom, ist, 32 Jahre alt.
Maria, ist, 32 Jahre alt.
Ihr, seid, 32 Jahre alt.
Tom und Maria, sind, 32 Jahre alt.
Ich, bin, nicht zu Hause.
Du, bist, nicht zu Hause.
Tom, ist, nicht zu Hause.
Maria, ist, nicht zu Hause.
Wir, sind, nicht zu Hause.
Ihr, seid, nicht zu Hause.
Tom und Maria, sind, nicht zu Hause.
Ich, bin, jetzt bereit.
Du, bist, jetzt bereit.
Tom, ist, jetzt bereit.
Maria, ist, jetzt bereit.
Wir, sind, jetzt bereit.
Ihr, seid, jetzt bereit.
Tom und Maria, sind, jetzt bereit.
Ich, bin, im Supermarkt.
Du, bist, im Supermarkt.
Tom, ist, im Supermarkt.
Maria, ist, im Supermarkt.
Wir, sind, im Supermarkt.
Ihr, seid, im Supermarkt.
Tom und Maria, sind, im Supermarkt.
Der Film, ist, sehr gut.
Das Buch, ist, interessant.
Das Wetter, ist, schön heute.
Die Pizza, ist, sehr lecker.
Das Auto, ist, zu laut.
Das Handy, ist, nicht teuer.
Das, ist, wichtig für mich.
Das, ist, eine gute Idee.
Das, ist, mein Lieblingsbuch.
""".strip()  # :contentReference[oaicite:0]{index=0}

sein_pairs = []
for line in sein_data.splitlines():
    prefix, verb, suffix = [p.strip() for p in line.split(",", 2)]
    sein_pairs.append({
        "prefix": prefix,
        "verb":   verb,
        "suffix": suffix
    })

# --- Y) Haben-Konjugation data ---
haben_data = """
Ich, habe, ein Problem.
Du, hast, ein Problem.
Tom, hat, ein Problem.
Maria, hat, ein Problem.
Wir, haben, ein Problem.
Ihr, habt, ein Problem.
Tom und Maria, haben, ein Problem.
Ich, habe, keine Zeit.
Du, hast, keine Zeit.
Tom, hat, keine Zeit.
Maria, hat, keine Zeit.
Wir, haben, keine Zeit.
Ihr, habt, keine Zeit.
Tom und Maria, haben, keine Zeit.
Ich, habe, ein neues Auto.
Du, hast, ein neues Auto.
Tom, hat, ein neues Auto.
Maria, hat, ein neues Auto.
Wir, haben, ein neues Auto.
Ihr, habt, ein neues Auto.
Tom und Maria, haben, ein neues Auto.
Ich, habe, eine Mikrowelle.
Du, hast, eine Mikrowelle.
Tom, hat, eine Mikrowelle.
Maria, hat, eine Mikrowelle.
Wir, haben, eine Mikrowelle.
Ihr, habt, eine Mikrowelle.
Tom und Maria, haben, eine Mikrowelle.
Ich, habe, viele Freunde.
Du, hast, viele Freunde.
Tom, hat, viele Freunde.
Maria, hat, viele Freunde.
Wir, haben, viele Freunde.
Ihr, habt, viele Freunde.
Tom und Maria, haben, viele Freunde.
Ich, habe, Hunger.
Du, hast, Hunger.
Tom, hat, Hunger.
Maria, hat, Hunger.
Wir, haben, Hunger.
Ihr, habt, Hunger.
Tom und Maria, haben, Hunger.
Ich, habe, eine schöne Wohnung.
Du, hast, eine schöne Wohnung.
Tom, hat, eine schöne Wohnung.
Maria, hat, eine schöne Wohnung.
Wir, haben, eine schöne Wohnung.
Ihr, habt, eine schöne Wohnung.
Tom und Maria, haben, eine schöne Wohnung.
Ich, habe, eine Frage.
Du, hast, eine Frage.
Tom, hat, eine Frage.
Maria, hat, eine Frage.
Wir, haben, eine Frage.
Ihr, habt, eine Frage.
Tom und Maria, haben, eine Frage.
Ich, habe, einen Hund.
Du, hast, einen Hund.
Tom, hat, einen Hund.
Maria, hat, einen Hund.
Wir, haben, einen Hund.
Ihr, habt, einen Hund.
Tom und Maria, haben, einen Hund.
Ich, habe, ein bisschen Fieber.
Du, hast, ein bisschen Fieber.
Tom, hat, ein bisschen Fieber.
Maria, hat, ein bisschen Fieber.
Wir, haben, ein bisschen Fieber.
Ihr, habt, ein bisschen Fieber.
Tom und Maria, haben, ein bisschen Fieber.
Ich, habe, viel Geduld.
Du, hast, viel Geduld.
Tom, hat, viel Geduld.
Maria, hat, viel Geduld.
Wir, haben, viel Geduld.
Ihr, habt, viel Geduld.
Tom und Maria, haben, viel Geduld.
Ich, habe, keinen deutschen Pass.
Du, hast, keinen deutschen Pass.
Tom, hat, keinen deutschen Pass.
Maria, hat, keinen deutschen Pass.
Wir, haben, keinen deutschen Pass.
Ihr, habt, keinen deutschen Pass.
Tom und Maria, haben, keinen deutschen Pass.
""".strip()

haben_pairs = []
for line in haben_data.splitlines():
    prefix, verb, suffix = [p.strip() for p in line.split(",", 2)]
    haben_pairs.append({
        "prefix": prefix,
        "verb":   verb,
        "suffix": suffix
    })

# --- Z) Temporale Adverbien (EN - DE) data ---
temporal_data = """
tomorrow, morgen
today, heute
yesterday, gestern
when, wann
since, seit
since when, seit wann
sometime, irgendwann
until, bis
never, nie
rarely, selten
sometimes, manchmal
often, oft
usually, normalerweise
always, immer
all the time, die ganze Zeit
briefly, kurz
now, jetzt
immediately, sofort
in a moment, gleich
one moment, einen Moment
soon, bald
before, vor
before that, davor
after, nach
after that, danach
early, früh
on time, pünktlich
late, spät
once, einmal
twice, zweimal
every, jede
still, immer noch
not yet, noch nicht
during, während
within, innerhalb
already, schon
again, wieder
over, vorbei
""".strip()

temporal_pairs = []
for line in temporal_data.splitlines():
    en, de = [p.strip() for p in line.split(",", 1)]
    temporal_pairs.append({
        "en": en,
        "de": de
    })

# --- Z) Lokale Adverbien (EN - DE) data ---
lokal_data = """
in front of, vor
in front of that, davor
behind, hinter
behind that, dahinter
next to, neben
next to that, daneben
below, unter
above, über
between, zwischen
at, bei
on, auf
to, zu
from, von
where, wo
where to, wohin
where from, woher
here, hier
there, dort
near, in der Nähe
far away, weit weg
everywhere, überall
somewhere, irgendwo
nowhere, nirgends
left, links
right, rechts
inside, drinnen
go inside, reingehen
outside, draußen
go outside, rausgehen
upstairs, oben
go upstairs, hochgehen
downstairs, unten
go downstairs, runtergehen
through, durch
""".strip()

lokal_pairs = []
for line in lokal_data.splitlines():
    en, de = [p.strip() for p in line.split(",", 1)]
    lokal_pairs.append({
        "en": en,
        "de": de
    })

# --- Z) Andere Adverbien (EN - DE) data ---
otheradv_data = """
completely, ganz
only, nur
very, sehr
also, auch
maybe, vielleicht
even, sogar
exactly, genau
approximately, circa
at least, mindestens
almost, fast
especially, vor allem
a little bit, ein bisschen
possible, möglich
possibly, möglicherweise
somehow, irgendwie
because of, wegen
that's why, deshalb
despite that, trotzdem
however, jedoch
but, aber
something, etwas
probably, wahrscheinlich
for sure, sicher
rather, lieber
simply, einfach
enough, genug
unfortunately, leider
once more, nochmal
by the way, übrigens
quite, ziemlich
alone, allein
together, zusammen
at first, zuerst
""".strip()

otheradv_pairs = []
for line in otheradv_data.splitlines():
    en, de = [p.strip() for p in line.split(",", 1)]
    otheradv_pairs.append({
        "en": en,
        "de": de
    })

# --- Z) Nomen Daten (EN - DE) data ---
nomenpers_data = """
the name, der Name
the last name, der Nachname
the first name, der Vorname
the age, das Alter
30 years old, 30 Jahre alt
the birthday, der Geburtstag
the year of birth, das Geburtsjahr
the place of birth, der Geburtsort
the number, die Nummer
the address, die Adresse
the street, die Straße
the city, die Stadt
the country, das Land
the countries, die Länder
the occupation, der Beruf
the school, die Schule
the schools, die Schulen
the employer, der Arbeitgeber
the postal code, die Postleitzahl
the language, die Sprache
the languages, die Sprachen
the native language, die Muttersprache
the signature, die Unterschrift
the nationality, die Nationalität
the insurance, die Versicherung
the application, der Antrag
the permit, die Genehmigung
the proof, der Nachweis
the form, das Formular
the ID, der Ausweis
to fill out, ausfüllen
to correct, korrigieren
to book, buchen
to send, schicken
to change, ändern
to check, prüfen
to tick, ankreuzen
to sign, unterschreiben
to register, sich anmelden
urgent, dringend
valid, gültig
male, männlich
female, weiblich
""".strip()

nomenpers_pairs = []
for line in nomenpers_data.splitlines():
    en, de = [p.strip() for p in line.split(",", 1)]
    nomenpers_pairs.append({
        "en": en,
        "de": de
    })

# --- Z) Nomen Ablauf (EN - DE) data ---
nomenablauf_data = """
the day, der Tag
the days, die Tage
the morning, der Morgen
the afternoon, der Nachmittag
the evening, der Abend
the breakfast, das Frühstück
the lunch, das Mittagessen
the dinner, das Abendessen
the alarm clock, der Wecker
the work, die Arbeit
the school, die Schule
the break, die Pause
the bed, das Bett
go to bed, ins Bett gehen
the mobile, das Handy
the movie, der Film
the series, die Serie
the clothing, die Kleidung
the jacket, die Jacke
the shoes, die Schuhe
to get up, aufstehen
to shower, duschen
to brush the teeth, die Zähne putzen
to clean, putzen
to tidy up, aufräumen
to watch, schauen
to learn, lernen
to put on, anziehen
to take off, ausziehen
to go, gehen
to go grocery shopping, einkaufen gehen
to go for a walk, spazieren gehen
to drive, fahren
to work, arbeiten
to call, anrufen
to eat, essen
to drink, trinken
to relax, sich entspannen
something, etwas
early, früh
late, spät
before, vor
after, nach
after that, danach
at 2 o'clock, um 2 Uhr
""".strip()

nomenablauf_pairs = []
for line in nomenablauf_data.splitlines():
    en, de = [p.strip() for p in line.split(",", 1)]
    nomenablauf_pairs.append({
        "en": en,
        "de": de
    })

# --- X) Sein-Präteritum data ---
waren_data = """
Ich, war, gestern in Basel.
Du, warst, gestern in Basel.
Tom, war, gestern in Basel.
Maria, war, gestern in Basel.
Wir, waren, gestern in Basel.
Ihr, wart, gestern in Basel.
Tom und Maria, waren, gestern in Basel.
Ich, war, vor dem Restaurant.
Du, warst, vor dem Restaurant.
Tom, war, vor dem Restaurant.
Maria, war, vor dem Restaurant.
Wir, waren, vor dem Restaurant.
Ihr, wart, vor dem Restaurant.
Tom und Maria, waren, vor dem Restaurant.
Ich, war, sehr freundlich.
Du, warst, sehr freundlich.
Tom, war, sehr freundlich.
Maria, war, sehr freundlich.
Wir, waren, sehr freundlich.
Ihr, wart, sehr freundlich.
Tom und Maria, waren, sehr freundlich.
Ich, war, letzte Woche im Büro.
Du, warst, letzte Woche im Büro.
Tom, war, letzte Woche im Büro.
Maria, war, letzte Woche im Büro. 
Wir, waren, letzte Woche im Büro.
Ihr, wart, letzte Woche im Büro.
Tom und Maria, waren, letzte Woche im Büro.
Ich, war, gestern nicht zu Hause.
Du, warst, gestern nicht zu Hause.
Tom, war, gestern nicht zu Hause.
Maria, war, gestern nicht zu Hause.
Wir, waren, gestern nicht zu Hause.
Ihr, wart, gestern nicht zu Hause.
Tom und Maria, waren, gestern nicht zu Hause.
Ich, war, gestern im Supermarkt.
Du, warst, gestern im Supermarkt.
Tom, war, gestern im Supermarkt.
Maria, war, gestern im Supermarkt.
Wir, waren, gestern im Supermarkt.
Ihr, wart, gestern im Supermarkt.
Tom und Maria, waren, gestern im Supermarkt.
Der Film, war, sehr gut.
Das Buch, war, interessant.
Das Wetter, war, gestern schön.
Die Pizza, war, sehr lecker.
Das Auto, war, zu laut.
Das Handy, war, nicht teuer.
Das, war, viel Arbeit.
Das, war, eine gute Idee.
Das, war, ein lustiger Film.
""".strip()  # :contentReference[oaicite:0]{index=0}

waren_pairs = []
for line in waren_data.splitlines():
    prefix, verb, suffix = [p.strip() for p in line.split(",", 2)]
    waren_pairs.append({
        "prefix": prefix,
        "verb":   verb,
        "suffix": suffix
    })

# --- Z) Nomen Haushalt (EN - DE) data ---
nomenhaushalt_data = """
the room, das Zimmer
the rooms, die Zimmer
the living room, das Wohnzimmer
the bathroom, das Badezimmer
the kitchen, die Küche
the hallway, der Flur
the stairs, die Treppen
the floor, der Stock
the lift, der Aufzug
the guest, der Gast
the guests, die Gäste
the toilet, die Toilette
the door, die Tür
the basement, der Keller
the balcony, der Balkon
the neighbor, der Nachbar
the neighbors, die Nachbarn
the table, der Tisch
the desk, der Schreibtisch
the chair, der Stuhl
the chairs, die Stühle
the sofa, das Sofa
the cabinet, der Schrank
the shelf, das Regal
the carpet, der Teppich
the wall, die Wand
the light, das Licht
the lamp, die Lampe
the bed, das Bett
the blanket, die Decke
the pillow, das Kopfkissen
the fridge, der Kühlschrank
the oven, der Backofen
the stove, der Herd
the microwave, die Mikrowelle
the dishwasher, die Spülmaschine
the washing machine, die Waschmaschine
the water heater, der Wasserkocher
the heater, die Heizung
to tidy up, aufräumen
to clean, putzen
to cook, kochen
to bake, backen
to turn on, anmachen
to turn off, ausmachen
to use, benutzen
comfortable, bequem
tidy, ordentlich
clean, sauber
dirty, dreckig
""".strip()

nomenhaushalt_pairs = []
for line in nomenhaushalt_data.splitlines():
    en, de = [p.strip() for p in line.split(",", 1)]
    nomenhaushalt_pairs.append({
        "en": en,
        "de": de
    })

# --- Z) Nomen Stadt (EN - DE) data ---
nomenstadt_data = """
the government office, das Amt
the church, die Kirche
the school, die Schule
the university, die Universität
the hospital, das Krankenhaus
the park, der Park
the cinema, das Kino
the store, das Geschäft
the supermarket, der Supermarkt
the hotel, das Hotel
the pharmacy, die Apotheke
the pharmacist, der Apotheker
the doctor's office, die Arztpraxis
the doctor, der Arzt
the airport, der Flughafen
the bank, die Bank
the train station, der Bahnhof
the train, der Zug
the timetable, der Fahrplan
the bus stop, die Haltestelle
the car, das Auto
the cars, die Autos
the motor bike, das Motorrad
the bicycle, das Fahrrad
the bicycles, die Fahrräder
the people, die Menschen
the police, die Polizei
the ambulance, der Krankenwagen
the tram, die Tram
the truck, der LKW
the street, die Straße
the path, der Weg
the square, der Platz
the pedestrian, der Fußgänger
the traffic light, die Ampel
the bridge, die Brücke
the building, das Gebäude
the buildings, die Gebäude
the sign, das Schild
the signs, die Schilder
the parking lot, der Parkplatz
the traffic, der Verkehr
the traffic jam, der Stau
the meadow, die Wiese
to drive, fahren
to stop, anhalten
to wait, warten
to sit, sitzen
""".strip()

nomenstadt_pairs = []
for line in nomenstadt_data.splitlines():
    en, de = [p.strip() for p in line.split(",", 1)]
    nomenstadt_pairs.append({
        "en": en,
        "de": de
    })

# --- Z) Nomen Arbeit (EN - DE) data ---
nomenarbeit_data = """
the office, das Büro
the monitor, der Bildschirm
the printer, der Drucker
the room, der Raum
the rooms, die Räume
the building, das Gebäude
the entrance, der Eingang
the exit, der Ausgang
the lift, der Aufzug
the stairs, die Treppen
the table, der Tisch
the desk, der Schreibtisch
the document, das Dokument
the documents, die Dokumente
the attachment, der Anhang
the colleague, der Kollege
the colleagues, die Kollegen
the appointment, der Termin
the appointments, die Termine
the project, das Projekt
the projects, die Projekte
the task, die Aufgabe
the tasks, die Aufgaben
the report, der Bericht
the file, die Datei
the schedule, der Zeitplan
the pen, der Stift
the piece of paper, das Blatt
the reminder, die Erinnerung
the message, die Nachricht
the messages, die Nachrichten
the conversation, das Gespräch
the meeting, die Besprechung
the visitor, der Besucher
the visitors, die Besucher
the superior, der Vorgesetzte
the boss, der Chef
the leader, der Leiter
the department, die Abteilung
the HR department, die Personalabteilung
the head of department, der Abteilungsleiter
the invitation, die Einladung
the decision, die Entscheidung
the reception, die Rezeption
the salary, das Gehalt
the promotion, die Beförderung
the breakfast, das Frühstück
the lunch, das Mittagessen
the break, die Pause
the opinion, die Meinung
to talk about, sprechen über
to send, schicken
to respond, antworten
to ask, fragen
to decide, entscheiden
to observe, beobachten
to check, prüfen
to ensure, sicherstellen
to have a break, eine Pause machen
responsible for, verantwortlich für
important, wichtig
urgent, dringend
together, zusammen
""".strip()

nomenarbeit_pairs = []
for line in nomenarbeit_data.splitlines():
    en, de = [p.strip() for p in line.split(",", 1)]
    nomenarbeit_pairs.append({
        "en": en,
        "de": de
    })

# --- Z) Nomen Golf (EN - DE) data ---
nomengolf_data = """
the club, der Schläger
the clubs, die Schläger
the iron, das Eisen
the rule, die Regel
the rules, die Regeln
the penalty, die Strafe
the player, der Spieler
the players, die Spieler
the game, das Spiel
the round, die Runde
the delay, die Verzögerung
the zone, der Bereich
the zones, der Bereiche
the shot, der Schlag
the target, das Ziel
the hole, das Loch
the flag, die Fahne
the tee, der Abschlag
the green, das Grün
the fairway, die Spielbahn
the sinking of the ball, das Einlochen
the size, die Größe
the brand, die Marke
the premises, das Gelände
the area, die Fläche
the penalty stroke, der Strafschlag
the glove, der Handschuh
the handicap, das Handicap
the stroke play, das Zählspiel
the match play, das Lochspiel
the exception, die Ausnahme
the obstacle, das Hindernis
the obstacles, die Hindernisse
the wind, der Wind
the gust of wind, die Windböe
the umbrella, der Regenschirm
the result, das Ergebnis
the distance, die Distanz
the map, die Karte
the pond, der Teich
the advantage, der Vorteil
the pit, die Grube
to switch, wechseln
to try, probieren
to use, benutzen
to take, nehmen
to take with, mitnehmen
to give, geben
to mark, markieren
to sink the ball, einlochen
to roll, rollen
to fly, fliegen
to search, suchen
to lose, verlieren
to find, finden
to hit, schlagen
to land, landen
short, kurz
long, lang
flat, flach
tief, low
high, hoch
straight, gerade
in the out, im Aus
wet, nass
dry, trocken
close, knapp
windy, windig
permitted, erlaubt
forbidden, verboten
on time, pünktlich
""".strip()

nomengolf_pairs = []
for line in nomengolf_data.splitlines():
    en, de = [p.strip() for p in line.split(",", 1)]
    nomengolf_pairs.append({
        "en": en,
        "de": de
    })

# --- X) Superlativ (Adjektive) data ---
super_data = """
laut, am lautesten
leise, am leisesten
schwierig, am schwierigsten
einfach, am einfachsten
schnell, am schnellsten
langsam, am langsamsten
schwer, am schwersten
leicht, am leichtesten
groß, am größten
klein, am kleinsten
alt, am ältesten
jung, am jüngsten
teuer, am teuersten
billig, am billigsten
heiß, am heißesten
kalt, am kältesten
scharf, am schärfsten
mild, am mildesten
sauber, am saubersten
schmutzig, am schmutzigsten
faul, am faulsten
fleißig, am fleißigsten
hell, am hellsten
dunkel, am dunkelsten
gut, am besten
schlecht, am schlechtesten
früh, am frühsten
spät, am spätesten
schön, am schönsten
lang, am längsten
kurz, am kürzesten
warm, am wärmsten
kühl, am kühlsten
spannend, am spannendsten
langweilig, am langweiligsten
hart, am härtesten
weich, am weichsten
reich, am reichsten
arm, am ärmsten
stark, am stärksten
schwach, am schwächsten
""".strip()

super_pairs = []
for line in super_data.splitlines():
    adj, comp = line.split(",", 1)
    super_pairs.append({
        "adj":  adj.strip(),
        "comp": comp.strip()
    })

# --- Y) Hatten-Konjugation data ---
hatten_data = """
Ich, hatte, letzte Woche ein Problem.
Du, hattest, letzte Woche ein Problem.
Tom, hatte, letzte Woche ein Problem.
Maria, hatte, letzte Woche ein Problem.
Wir, hatten, letzte Woche ein Problem.
Ihr, hattet, letzte Woche ein Problem.
Tom und Maria, hatten, letzte Woche ein Problem.
Ich, hatte, gestern keine Zeit.
Du, hattest, gestern keine Zeit.
Tom, hatte, gestern keine Zeit.
Maria, hatte, gestern keine Zeit.
Wir, hatten, gestern keine Zeit.
Ihr, hattet, gestern keine Zeit.
Tom und Maria, hatten, gestern keine Zeit.
Ich, hatte, einen Autounfall.
Du, hattest, einen Autounfall.
Tom, hatte, einen Autounfall.
Maria, hatte, einen Autounfall.
Wir, hatten, einen Autounfall.
Ihr, hattet, einen Autounfall.
Tom und Maria, hatten, einen Autounfall.
Ich, hatte, als Kind einen Game-Boy.
Du, hattest, als Kind einen Game-Boy.
Tom, hatte, als Kind einen Game-Boy.
Maria, hatte, als Kind einen Game-Boy.
Wir, hatten, als Kind einen Game-Boy.
Ihr, hattet, als Kind einen Game-Boy.
Tom und Maria, hatten, als Kind einen Game-Boy.
Ich, hatte, den ganzen Tag Hunger.
Du, hattest, den ganzen Tag Hunger.
Tom, hatte, den ganzen Tag Hunger.
Maria, hatte, den ganzen Tag Hunger.
Wir, hatten, den ganzen Tag Hunger.
Ihr, hattet, den ganzen Tag Hunger.
Tom und Maria, hatten, den ganzen Tag Hunger.
Ich, hatte, eine schöne Wohnung.
Du, hattest, eine schöne Wohnung.
Tom, hatte, eine schöne Wohnung.
Maria, hatte, eine schöne Wohnung.
Wir, hatten, eine schöne Wohnung.
Ihr, hattet, eine schöne Wohnung.
Tom und Maria, hatten, eine schöne Wohnung.
Ich, hatte, früher einen Hund.
Du, hattest, früher einen Hund.
Tom, hatte, früher einen Hund.
Maria, hatte, früher einen Hund.
Wir, hatten, früher einen Hund.
Ihr, hattet, früher einen Hund.
Tom und Maria, hatten, früher einen Hund.
Ich, hatte, ein bisschen Fieber.
Du, hattest, ein bisschen Fieber.
Tom, hatte, ein bisschen Fieber.
Maria, hatte, ein bisschen Fieber.
Wir, hatten, ein bisschen Fieber.
Ihr, hattet, ein bisschen Fieber.
Tom und Maria, hatten, ein bisschen Fieber.
Ich, hatte, früher viel Geduld.
Du, hattest, früher viel Geduld.
Tom, hatte, früher viel Geduld.
Maria, hatte, früher viel Geduld.
Wir, hatten, früher viel Geduld.
Ihr, hattet, früher viel Geduld.
Tom und Maria, hatten, früher viel Geduld.
Ich, hatte, als Kind kein Handy.
Du, hattest, als Kind kein Handy.
Tom, hatte, als Kind kein Handy.
Maria, hatte, als Kind kein Handy.
Wir, hatten, als Kind kein Handy.
Ihr, hattet, als Kind kein Handy.
Tom und Maria, hatten, als Kind kein Handy.
""".strip()

hatten_pairs = []
for line in hatten_data.splitlines():
    prefix, verb, suffix = [p.strip() for p in line.split(",", 2)]
    hatten_pairs.append({
        "prefix": prefix,
        "verb":   verb,
        "suffix": suffix
    })

# --- Z) Nomen Gesundheit (EN - DE) data ---
nomengesund_data = """
the pharmacy, die Apotheke
the doctor, der Arzt
the dentist, der Zahnarzt
the medication, das Medikament
the prescription, das Rezept
the pill, die Tablette
the pills, die Tabletten
the pain, die Schmerzen
the painkiller, das Schmerzmittel
the examination, die Untersuchung
the cold, die Erkältung
the cough, der Husten
the fever, das Fieber
the head, der Kopf
the tooth, der Zahn
the teeth, die Zähne
the tooth brush, die Zahnbürste
the tooth paste, die Zahnpasta
the comb, der Kamm
the mirror, der Spiegel
the ointment, die Salbe
the cream, die Creme
the deodorant, das Deo
the perfume, das Parfüm
the vaccination, die Impfung
the skin, die Haut
the soap, die Seife
the hand, die Hand
the hands, die Hände
the towel, das Handtuch
the cloth, das Tuch
the handkerchief, das Taschentuch
the bag, die Tasche
to cough, husten
to sneeze, niesen
to wash, waschen
to clean, putzen
to comb, kämmen
to shower, duschen
to bath, baden
to examine, untersuchen
to rub on, einreiben
to apply, auftragen
to spray, sprühen
to dry, trocknen
to put make-up on, schminken
thoroughly, gründlich
carefully, vorsichtig
painful, schmerzhaft
daily, täglich
clean, sauber
dirty, dreckig
dry, trocken
wet, nass
""".strip()

nomengesund_pairs = []
for line in nomengesund_data.splitlines():
    en, de = [p.strip() for p in line.split(",", 1)]
    nomengesund_pairs.append({
        "en": en,
        "de": de
    })

# --- Z) Nomen Natur (EN - DE) data ---
nomennatur_data = """
the tree, der Baum
the trees, die Bäume
the forest, der Wald
the weather, das Wetter
the rain, der Regen
the snow, der Schnee
the cloud, die Wolke
the thunderstorm, das Gewitter
the lightning, der Blitz
the thunder, der Donner
the fog, der Nebel
the sky, der Himmel
the sun, die Sonne
the moon, der Mond
the stars, die Sterne
the flower, die Blume
the flowers, die Blumen
the meadow, die Wiese
the path, der Weg
the bridge, die Brücke
the hill, der Hügel
the mountain, der Berg
the mountains, die Berge
the hut, die Hütte
the valley, das Tal
the stream, der Bach
the river, der Fluss
the lake, der See
the sea, das Meer
the animal, das Tier
the bird, der Vogel
the wind, der Wind
the gust of wind, die Windböe
to rain, regnen
to snow, schneien
to hike, wandern
to swim, schwimmen
to ski, Ski fahren
hot, heiß
cold, kalt
sunny, sonnig
cloudy, bewölkt
foggy, neblig
windy, windig
rainy, regnerisch
green, grün
blue, blau
grey, grau
""".strip()

nomennatur_pairs = []
for line in nomennatur_data.splitlines():
    en, de = [p.strip() for p in line.split(",", 1)]
    nomennatur_pairs.append({
        "en": en,
        "de": de
    })

@app.route('/nomennatur')
def nomennatur():
    return render_template('nomenablauf.html', pairs=nomennatur_pairs)

@app.route('/nomengesund')
def nomengesund():
    return render_template('nomenablauf.html', pairs=nomengesund_pairs)

@app.route('/hatten')
def hatten():
    return render_template('hatten.html', pairs=hatten_pairs)

@app.route('/super')
def super():
    return render_template('super.html', pairs=super_pairs)

@app.route('/nomengolf')
def nomengolf():
    return render_template('nomenablauf.html', pairs=nomengolf_pairs)

@app.route('/nomenarbeit')
def nomenarbeit():
    return render_template('nomenablauf.html', pairs=nomenarbeit_pairs)

@app.route('/nomenstadt')
def nomenstadt():
    return render_template('nomenablauf.html', pairs=nomenstadt_pairs)

@app.route('/nomenhaushalt')
def nomenhaushalt():
    return render_template('nomenablauf.html', pairs=nomenhaushalt_pairs)

@app.route('/waren')
def waren():
    return render_template('waren.html', pairs=waren_pairs)

@app.route('/nomenablauf')
def nomenablauf():
    return render_template('nomenablauf.html', pairs=nomenablauf_pairs)

@app.route('/nomenpers')
def nomenpers():
    return render_template('nomenablauf.html', pairs=nomenpers_pairs)

@app.route('/otheradv')
def otheradv():
    return render_template('nomenablauf.html', pairs=otheradv_pairs)

@app.route('/lokal')
def lokal():
    return render_template('nomenablauf.html', pairs=lokal_pairs)

@app.route('/temporal')
def temporal():
    return render_template('nomenablauf.html', pairs=temporal_pairs)

@app.route('/haben')
def haben():
    return render_template('haben.html', pairs=haben_pairs)

@app.route('/sein')
def sein():
    return render_template('sein.html', pairs=sein_pairs)

@app.route('/rechner')
def rechner():
    return render_template('rechner.html')

@app.route('/trennbare_verben')
def trennbare_verben():
    return render_template('trennbar.html', pairs=trennbar_pairs)

@app.route('/fragen')
def fragen():
    options = ["wo","woher","wohin","was","wann","seit wann","wer","wie","welche","warum"]
    return render_template('fragen.html', pairs=fragen_pairs, options=options)

@app.route('/konjugation2')
def konjugation2():
    return render_template('konjugation2.html', pairs=konj2_pairs)

@app.route('/konjugation')
def konjugation():
    return render_template('konjugation.html', pairs=konj_pairs)

@app.route('/perfekt')
def perfekt():
    return render_template('perfekt.html', pairs=perfekt_pairs)

@app.route('/steigerung')
def steigerung():
    return render_template('steigerung.html', pairs=steigerung_pairs)

@app.route('/')
def home():
    return render_template('menu.html')

@app.route('/artikelregeln')
def artikelregeln():
    return render_template('artikel.html', words=words)

@app.route('/gegenteile_adjektive')
def gegenteile_adjektive():
    return render_template('gegenteile_adjektive.html', pairs=adj_pairs)

@app.route('/gegenteile_verben')
def gegenteile_verben():
    return render_template('gegenteile_verben.html', pairs=verb_pairs)

@app.route('/verbenfall')
def verbenfall():
    return render_template('verben_fall.html', pairs=case_pairs)

@app.route('/personalpronomen')
def personalpronomen():
    return render_template('personalpronomen.html', pairs=personal_pairs)

@app.route('/modalverben')
def modalverben():
    return render_template('modal.html', pairs=modal_pairs)


if __name__ == '__main__':
    app.run(debug=True)