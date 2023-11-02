import re

def break_into_lines(long_text, max_line_length=80):

    words = long_text.split(' ')
    lines = []
    current_line = ''

    for word in words:
        if len(current_line) + len(word) + 1 > max_line_length:
            lines.append(current_line)
            current_line = ''

        if current_line:
            current_line += ' '

        current_line += word

    lines.append(current_line)
    return '\n'.join(lines)

# Read the text from the file with utf-8 encoding
with open('termstext.txt', 'r', encoding='utf-8') as f:
    termsTextLongLine = f.read()

# Your long text goes here
termsTextLongLine = """B.6 Motor och elektronik för personbil, lätt lastbil och husbil
Vad försäkringen gäller för
Bilen får ha varit registrerad i högst 8 år från första registreringsdatumet. Bilen får ha körts
högst
• privatägd personbil/lätt lastbil 12 000 mil
• privatägd och företagsägd husbil 12 000 mil
• företagsägd personbil/lätt lastbil 15 000 mil
Försäkringen upphör så snart någon av gränserna uppnåtts. Ägaren ska styrka bilens ålder
och antalet körda mil.
Kan det inte visas vilken dag skadan uppstod, anses händelsen ha inträffat den dag anmälan kommit till oss.
24 | B – Allmänna villkor
P00297_2204
Vad försäkringen inte gäller för
Försäkringen gäller inte för skada som ska ersättas enligt lag, garanti (till exempel
MRF-Garanti), eller annat åtagande.
Vad du får ersättning för
Det här Men inte det här
Inifrån kommande skada eller fel som påverkar
bilens funktion.
Kostnader utöver självrisken för undersökning och
demontering, som vi i förväg godkänt, i syfte att
fastställa om skadan ersätts av försäkringen.
Skada som orsakats av
• frysning, väta eller korrosion
• förorenat bränsle
Servicedetaljer och komponenter som behöver bytas
vid reparation och som inte tillhör den aktuella skadan
ersätts inte.
Vagn-, brand-, glasrute, drulle- eller stöldskada som
kan ersättas genom respektive försäkringsmoment.
Hopsättning och återmontering efter undersökning
och demontering, där skadan inte ersätts av försäkringen.
Fabrikations-, material, konstruktionsfel eller
definierade och fastställda seriefel.
B – Allmänna villkor | 25
P00297_2204
Det här Men inte det här
Inifrån kommande skada eller fel som påverkar
bilens funktion och som berör någon av följande
komponenter:
Motor och kylsystem
• avgasturbo, laddluftkylare, överladdningsaggregat
inklusive styrsystem
• bränslesystem inklusive insprutningssystem och
dess reglerfunktioner
• grenrör
• defrosterslingor i rutor
• klimatanläggning
• motorvärmare som är integrerad i bilens
kyl/värmesystem
• motorns kylsystem
• motor och elmotor,inklusive dess styrelektronik,
för framdrift av fordonet
• elektroniskt tänd- och rattlås
• startmotor inklusive tändningsnyckel/kort/smartkey, start/stopsystem
• system för avgasrening inklusive dess styrsystem
• tändsystem och dess reglerfunktioner
Växellåda och kraftöverföring
• drivaxlar
• tryckplatta och svänghjul
• kraftöverföring, växellåda, styrelektronik och
reglage
Skada på:
Motor och kylsystem
• bränsleledningar, filter, bränsletank
• ljuddämpare och avgasrör
• tändstift och startbatteri
• mekaniskt tänd- och rattlås
Växellåda och kraftöverföring
• hjullager
• lamellbelägg och följdskador av detta
• växellåde- och kopplingsvajer
26 | B – Allmänna villkor
P00297_2204
Det här Men inte det här
Inifrån kommande skada eller fel som påverkar
bilens funktion och som berör någon av följande
komponenter:
Elektronik
• central elektronikmodul och elcentral med
säkringsdosa
• centrallåsenhet
• elektriska kablar
• elektroniskt stöldskydd och larm
• flerfunktion/kombinationsinstrument, (exempelvis
hastighetsmätare och motorinformation)
• färddator och farthållare
• generator och följdskador som påverkar bilens
elektroniska funktion
• informations- och kommunikationssystem för data,
navigering och multimedia (fabriksmonterad)
• motor till cabriolet, bak- och taklucka
• regnsensorer
• stolsvärmare
• styrenhet till stol, fönster och centrallås samt
motorer till dessa
• torkarmotor till vind- och bakruta
• klimatanläggning för husbilsbodel (fabriksmonterad )
• vitvaror för husbil (fabriksmonterad)
• värmepanna för husbil (fabriksmonterad)
Broms, styrning
• servosystem för bromsar inklusive huvudcylindrar
• servosystem för styrinrättning
• styr- och reglersystem för låsningsfria bromsar
• styrväxel
Skada på:
Broms, styrning
• hjulcylindrar, bromsok, bromsskivor/trummor och
bromsbelägg
• stag och kulleder
B – Allmänna villkor | 27
P00297_2204
Det här Men inte det här
Inifrån kommande skada eller fel som påverkar
bilens funktion och som berör någon av följande
komponenter:
Säkerhets och förarstödsystem
• akustiskt fordonsvarningssystem (fabriksmonterat)
• antisladd och spinnsystem samt elektronik till
chassiestabiliseringssystem
• airbag inklusive givare och sensorer
• kollisionsvarningssystem och autobromssystem
• line- och sideassistsystem
• luftfjädring, pump och bälg
• parkeringsassistans
• reglermotor till adaptiva strålkastare
• styrenhet till Xenon, LED och laserljus
• säkerhetsbälte, bältespåminnare och bältesförsträckare
• säkerhetslarm och gasvarnare för husbil
Hybriddrift
• ac/dc-omvandlare (fabriksmonterad)
• batteri för framdrivning av fordonet
• elmotor för framdrivning av fordonet av fordonet
• högvoltskablage (fabriksmonterat)
• kylsystem för högvoltssystem
• laddningsenhet för högvoltsbatteri (fabriksmonterad on-board charger)
• solcellsystem (fabriksmonterat)
• styrdon för eldrift
Skada på:
Säkerhets och förarstödsystem
• ljuskälla och lyktglas
• stötdämpare och fjädrar
• dörrlåsmekanik
Hybriddrift
• laddkabel med eller utan extern laddenhet
• lågvoltsbatteri
28 | B – Allmänna villkor
P00297_2204
Det här Men inte det här
Inifrån kommande skada eller fel som påverkar
bilens funktion och som berör någon av följande
komponenter:
Eldrift
• ac/dc-omvandlare (fabriksmonterad)
• batteri för framdrivning av fordonet
• elmotor för framdrivning av fordonet
• högvoltskablage (fabriksmonterat)
• kylsystem för högvoltssystem
• laddningsenhet för högvoltsbatteri (fabriksmonterad on-board charger)
• solcellsystem (fabriksmonterat)
• styrdon för eldrift
Skada på:
Eldrift
• laddkabel med eller utan extern laddenhet
• lågvoltsbatteri
Aktsamhetskrav/säkerhetsföreskrift
• Bilen får inte köras så att motor eller kraftöverföring utsätts för onormal påfrestning,
exempelvis fortsätta köra om ett läckage av olja eller kylarvätska har uppstått eller köra
fast varningslampa har tänts.
• Komponenter och mjukvara som avviker från fordonets seriemässiga utförande får inte
användas.
• Luftventiler för kylning av batterier får inte blockeras, exempelvis med stolsöverdrag,
så att batteriet överhettas.
Om aktsamhetskraven/säkerhetsföreskrifter inte följs
Ersättningen minskas, normalt med 25 %. För näringsidkare kan ersättningen minskas eller
helt utebli. Regler om nedsättning av ersättning finns i avsnitt G.4 Begränsningar i vårt ansvar.
Garanti för begagnade delar
Om en skada regleras genom att begagnad del monteras, lämnar vi garanti motsvarande
sedvanlig garanti från branschverkstad. Garantin gäller under 6 månader men i högst 1 000
körda mil.
Garantifall måste genast anmälas till oss. Vi förbehåller oss rätten att besiktiga bilen före
reparation.
B – Allmänna villkor | 29
P00297_2204
Självrisk
Privatägd personbil, lätt lastbil och privatägd/företagsägd husbil
Bilen har körts:
• högst 4 000 mil 1 500 kronor
• högst 10 000 mil 5 000 kronor
• högst 12 000 mil 8 000 kronor
Företagsägd personbil och lätt lastbil
Bilen har körts:
• högst 4 000 mil 10 % av prisbasbeloppet
• högst 5 000 mil 20 % av skadekostnaden, lägst 10 % av prisbasbeloppet
• högst 7 000 mil 30 % av skadekostnaden, lägst 10 % av prisbasbeloppet
• högst 10 000 mil 40 % av skadekostnaden, lägst 10 % av prisbasbeloppet
• högst 15 000 mil 50 % av skadekostnaden, lägst 10 % av prisbasbeloppet
B.7 Motor och elektronik för husvagn
Vad försäkringen gäller för
Privat- och företagsägd husvagn. Husvagnen får ha varit registrerad i högst 8 år från första
registreringsdatumet. Ägaren ska styrka husvagnens ålder. Kan det inte visas vilken dag
skadan uppstod, anses händelsen ha inträffat den dag anmälan kommit till oss.
Vad försäkringen inte gäller för
Försäkringen gäller inte
• för skada som ska ersättas enligt lag, garanti eller annat åtagande
• för husvagn i yrkesmässig uthyrning.
30 | B – Allmänna villkor
P00297_2204
Vad du får ersättning för
Det här Men inte det här
Inifrån kommande skada eller fel på
• elektroblock
• hydrauliska stödben inklusive motorer
• värmepanna
• varmvattenberedare
• larm och gasvarnare
• vitvaror
• klimatanläggning för husvagnens bodel
(fabriksmonterad).
Skada som orsakats av
• Frysning, väta eller korrosion
• Servicedetaljer och komponenter som behöver
bytas vid reparation och som inte tillhör den
aktuella skadan ersätts inte.
• Vagn-, brand-, glasrute, drulle- eller stöldskada som
kan ersättas genom respektive försäkringsmoment.
• Hopsättning och återmontering efter undersökning
och demontering, där skadan inte ersätts av
försäkringen.
• Fabrikations-, material, konstruktionsfel eller
definierade och fastställda seriefel.
Självrisk
1 500 kronor"""

# Break the text into lines of maximum length 80
termsTextLongLineFormatted = break_into_lines(termsTextLongLine)

# Remove chapter headings
cleaned_text = re.sub(r'B\.\s+Allmänna\s+villkor\s*\|\s*\d+', '', termsTextLongLineFormatted)

# Remove page identifiers
termsTextLongLineFormatted = re.sub(r'P\d+_\d+', '', cleaned_text)

termsTextLongLineFormatted.strip()


# Write the formatted text back to a file with utf-8 encoding
with open('formatted_text.txt', 'w', encoding='utf-8') as f:
    f.write(termsTextLongLineFormatted)


break_into_lines(termsTextLongLineFormatted, max_line_length=80)






