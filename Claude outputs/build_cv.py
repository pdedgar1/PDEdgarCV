"""Build cv.json from P.D. Edgar's CV.

Each block below mirrors one H1 section of the CV, so you can edit a
section without touching the rest. Helpers:
  S(title, cat)        start an H1 section (cat = default category)
  U(title, cat=None)   start an H2 subsection (optionally new default category)
  H(title)             start an H3 heading within the subsection
  E(type, title, ...)  add one entry
Dates: d = text exactly as written in the CV; s / e = sortable start / end
("YYYY", "YYYY-MM" or "YYYY-MM-DD"); on=True for ongoing; st = explicit status.
"""
import json, re

TODAY = "2026-11-13"
D = {"meta": {}, "sections": [], "entries": []}
cur = {"sec": None, "sub": None, "h3": None, "sec_cat": None, "cat": None}


def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def S(title, cat):
    cur.update(sec=title, sub=None, h3=None, sec_cat=cat, cat=cat)
    D["sections"].append({"id": slug(title)[:48], "title": title, "order": len(D["sections"]) + 1})


def U(title, cat=None):
    cur.update(sub=title, h3=None, cat=cat or cur["sec_cat"])


def H(title):
    cur["h3"] = title


def E(type, title, d="", s=None, e=None, st=None, on=False, role=None, venue=None,
      loc=None, det=None, links=None, grp=None, cat=None, note=None):
    n = len(D["entries"]) + 1
    if st:
        status = st
    elif on:
        status = "ongoing"
    elif s or e:
        status = "upcoming" if max(x for x in (s, e) if x) > TODAY else "completed"
    else:
        status = None
    D["entries"].append({
        "id": f"{n:03d}-{slug(title)[:40]}",
        "order": n,
        "section": slug(cur["sec"])[:48],
        "subsection": cur["sub"],
        "heading": cur["h3"],
        "group": grp,
        "type": type,
        "category": cat or cur["cat"],
        "title": title,
        "role": role,
        "venue": venue,
        "location": loc,
        "details": det or [],
        "links": [{"label": l, "url": u} for l, u in (links or [])],
        "date": {"display": d, "start": s, "end": e, "ongoing": on, "status": status},
        "note": note,
    })


# ---------------------------------------------------------------- header
D["meta"] = {
    "title": "Curriculum Vitae - P.D. Edgar - Ph.D. Candidate",
    "name": "P.D. Edgar",
    "position": "Ph.D. Candidate",
    "email": "pe840191@ucf.edu",
    "website": "http://pdedgar.xyz",
    "handle": "@PDEdgar30",
    "source": "Curriculum_Vitae_-_PD_Edgar_11_26.md",
    "generated": TODAY,
}

# ---------------------------------------------------------------- Education
S("Education", "Education & Training")
U("Ph.D. Candidate : Texts & Technology : University of Central Florida, Orlando, FL")
H("Digital Media Concentration ABD")
E("degree", "Ph.D., Texts & Technology", d="ABD", on=True, role="Ph.D. Candidate",
  venue="University of Central Florida", loc="Orlando, FL", det=["Digital Media Concentration", "ABD"])
E("fellowship", "4-year Trustees Doctoral Fellowship", d="2024-2028", s="2024", e="2028", on=True,
  venue="University of Central Florida", cat="Recognition & Funding")
E("fellowship", "Summer Mentoring Fellowship", d="2024", s="2024-06", e="2024-08",
  venue="University of Central Florida", cat="Recognition & Funding")
E("dissertation", "How Literary Magazine Editors’ Submissions Processes are Changing in the Age of AI",
  role="Dissertation proposal", cat="Scholarly")
U("Graduate Certificate - Digital Humanities in the Age of AI")
E("certificate", "Graduate Certificate - Digital Humanities in the Age of AI",
  d="Completed Summer 2026", s="2026-06", e="2026-08",
  venue="University of Central Florida")
U("M.F.A. Creative Writing : University of Alabama, Tuscaloosa, AL")
E("degree", "M.F.A. Creative Writing", venue="University of Alabama", loc="Tuscaloosa, AL",
  det=["Thesis Track: Hybrid Memoir (Poetry & Nonfiction)",
       "Thesis: “Dispatches from the Mission House : Scriptures of an Ex-MK”"])
U("M.A. Journalism & Media Studies : University of Alabama, Tuscaloosa, AL")
E("degree", "M.A. Journalism & Media Studies", venue="University of Alabama", loc="Tuscaloosa, AL",
  det=["Winner, Outstanding Graduate Journalism Thesis Award",
       "Thesis: “their concept of beauty / is manufactured / i am not -rupi kaur”: How Remediation Theory "
       "Reconciles Instapoetry’s Genre, Branded Authenticities, and Critical Positionality"])
U("B.A. Florida Southern College, Lakeland, FL")
E("degree", "B.A.", venue="Florida Southern College", loc="Lakeland, FL",
  det=["Majors in English: Writing | Communications: Multimedia Journalism | Spanish",
       "Summa Cum Laude w. Honors | Hollingsworth Scholarship recipient (Full Scholarship)"])

# ---------------------------------------------------------------- Editorial
S("Editorial Experience", "Editorial & Publishing")
U(None)
ccc = [("College Composition and Communication", "https://cccc.ncte.org/cccc/ccc")]
E("editorial-role", "College Composition and Communication", d="Aug ‘25-present", s="2025-08", on=True,
  role="Editorial Assistant", venue="peer-reviewed journal", grp="ccc", links=ccc,
  det=["Production, Research, Communication, Administrative Tasks", "Began the CCC Editors’ Instagram Account"])
E("editorial-role", "College Composition and Communication", d="Aug ‘24-May ‘25", s="2024-08", e="2025-05",
  role="Editorial Assistant", venue="peer-reviewed journal", grp="ccc", links=ccc)
E("editorial-role", "re•mediate", d="May 2024 - present", s="2024-05", on=True, role="Founding Editor",
  venue="literary magazine, online", links=[("re•mediate", "https://remediatelitmag.xyz")],
  det=["Issue•0 through Issue•7",
       "Collaborated with Invited Guest Editors: Monica Storss, Benjamin Escalonilla"])
E("editorial-role", "The Florida Review", d="Dec. ‘25-Feb ’26", s="2025-12", e="2026-02",
  role="Manuscript reader", venue="literary journal, Univ. of Central Florida",
  links=[("The Florida Review", "https://cah.ucf.edu/floridareview/"),
         ("Jeanne Leiby Memorial Chapbook Award", "https://cah.ucf.edu/floridareview/submit/chapbook-contest/")],
  det=["2026 Jeanne Leiby Memorial Chapbook Award", "Two of my selections made the semifinals"])
E("editorial-role", "Kenyon Review", d="June 2023 – May 2024", s="2023-06", e="2024-05",
  role="Digital Archive Associate", venue="literary magazine, Kenyon College, Ohio",
  links=[("Kenyon Review archive", "https://kenyonreview.org/the-archive/")],
  det=["Converted PDF copies of KR to WordPress"])
bwr = [("Black Warrior Review", "https://bwr.ua.edu")]
bv = "graduate-run literary magazine, Univ. of Alabama"
E("editorial-role", "Black Warrior Review", d="Jan. ‘22– Apr. ‘24", s="2022-01", e="2024-04",
  role="Assistant Editor, Poetry + Nonfiction + Fiction", venue=bv, grp="bwr", links=bwr)
E("editorial-role", "Black Warrior Review", d="Jan.’22–Dec.’24", s="2022-01", e="2024-12",
  role="Art & Design Editor", venue=bv, grp="bwr", links=bwr,
  det=["Issues 48.2, 49.1, 49.2, 50.1, and 50.2"])
E("editorial-role", "Black Warrior Review", d="Fall ‘20 – ‘21", s="2020-08", e="2021",
  role="Assistant Editor, Poetry + Nonfiction", venue=bv, grp="bwr", links=bwr)

# ---------------------------------------------------------------- Teaching
S("Teaching Experience", "Teaching & Pedagogy")
U("Florida Southern College, Adjunct Professor")
H("Communications Department")
E("course-taught", "COM 1500-1EB: Speech for Success", d="FallB 2025 - FallB 2026 (3x)", s="2025-10",
  e="2026-12", on=True, venue="Florida Southern College", det=["Online Class", "Taught 3x"])
U("University of Alabama, Instructor of Record (Graduate Teaching Assistantship)")
H("First-Year Writing Program")
E("course-taught", "EN 101 - Narrative Writing", d="Fall 2021", s="2021-08", e="2021-12",
  venue="University of Alabama", grp="en101")
E("course-taught", "EN 101 - Narrative Writing", d="Spring 2024", s="2024-01", e="2024-05",
  venue="University of Alabama", grp="en101")
E("course-taught", "EN 102 - Research Writing", d="Spring 2022", s="2022-01", e="2022-05",
  venue="University of Alabama", det=["Theme: “Hidden in Plain Sight”"])
E("course-taught", "EN 103 - Honors Composition", d="Fall 2023", s="2023-08", e="2023-12",
  venue="University of Alabama", det=["Theme: “Writing about Crisis”"])
H("Creative Writing")
E("course-taught", "EN 200 - Introduction to Creative Writing", d="Spring 2023", s="2023-01", e="2023-05",
  venue="University of Alabama")
E("course-taught", "EN 308 - Creative Nonfiction Workshop", d="Spring 2024", s="2024-01", e="2024-05",
  venue="University of Alabama")
U("University of Alabama, Writing Center, Tuscaloosa, AL")
E("tutoring", "Writing Center Tutor", d="Aug 2020 - May 2021", s="2020-08", e="2021-05",
  venue="University of Alabama Writing Center", loc="Tuscaloosa, AL")
E("tutoring", "Dissertation Writing Challenge Group Leader", d="May 2 - June 30, 2021",
  s="2021-05-02", e="2021-06-30", venue="University of Alabama Writing Center", grp="dwc")
E("tutoring", "Dissertation Writing Challenge Group Leader", d="Sept. 16 - Oct. 28, 2020",
  s="2020-09-16", e="2020-10-28", venue="University of Alabama Writing Center", grp="dwc")
U("Proyecto Español, Alicante, Spain")
E("internship", "Language School Intern", d="Summer 2018", s="2018-06", e="2018-08",
  venue="Proyecto Español", loc="Alicante, Spain", det=["English Tutor, English Camp Leader, Marketing"])

# ---------------------------------------------------------------- Research Interests
S("Research Interests", "Scholarly")
U(None)
for t in ["Emerging Media (AI, Virtual Reality, Social Media)",
          "Literary Print Culture (Magazines, Little Mags, Pop Literature)",
          "Creative Writing (Pedagogy, Poetry & Nonfiction)",
          "Literary Production/Industry (Publishing, Paratexts, Networks)"]:
    E("research-interest", t)

# ---------------------------------------------------------------- Digital Projects
S("Digital Projects", "Creative")
U(None)
E("digital-project", "re•mediate n•human", d="October 1 - November 1, 2026", s="2026-10-01", e="2026-11-01",
  links=[("re•mediate n•human", "http://remediatelitmag.xyz/nhuman")],
  det=["A zine of unsolicited work submitted by AI Agents",
       "From October 1 - November 1, I declined to decline “creative writing” by AI agents that came into my "
       "inbox at the literary magazine I run. Instead, for the public’s “benefit” (visibility, raising awareness "
       "about what AI-generated “creative writing” looks like), I published them all on a webpage."])
E("digital-project", "E-Lit Journals Borderlands", on=True, cat="Scholarly",
  links=[("E-Lit Journals Borderlands", "https://pdedgar1.github.io/ELitJournals/")],
  det=["Early version presented at Modernism Studies Conference",
       "An ongoing repository of the bylines of publications that do computer-inflected writing."])
E("digital-project", "The Text Kitchen",
  links=[("The Text Kitchen", "https://pdedgar1.github.io/Text-Kitchen/"),
         ("Potluck Zine", "http://remediatelitmag.xyz/offgrid")],
  det=["Presented at the New Media Writing Prize Unconference",
       "Potluck Zine, a collection of work created with the Text Kitchen"])

# ---------------------------------------------------------------- Publications
S("Publications", "Creative")
U("Interviews", "Editorial & Publishing")
pq = "periodicities: a journal of poetry and poetics"
E("interview", "Katherine Parrish: Conversations with P.D. Edgar, part two", d="Nov 5, 2025", s="2025-11-05",
  venue=pq, grp="parrish",
  links=[("Read", "https://periodicityjournal.blogspot.com/2025/11/katherine-parrish-conversations-with-pd_01442627467.html")])
E("interview", "Katherine Parrish: Conversations with P.D. Edgar, part one", d="Nov 4, 2025", s="2025-11-04",
  venue=pq, grp="parrish",
  links=[("Read", "https://periodicityjournal.blogspot.com/2025/11/katherine-parrish-conversations-with-pd.html")])
U("Book Reviews", "Editorial & Publishing")
E("book-review", "The Kenyon Review’s 2024 Summer Reading Recommendations", d="May 29, 2024", s="2024-05-29",
  venue="The Kenyon Review", det=["Our Air by Nora Treatbaby"],
  links=[("Read", "https://kenyonreview.org/2024/05/2024-summer-reading-recommendations/")])
U("Creative Writing")
E("creative-publication", "THREAD 🧵/7", d="Sept. 23, 2026", s="2026-09-23", venue="Seam Allowance",
  det=["poem"], links=[("Instagram", "https://www.instagram.com/p/DdrQfX7lela/")])
E("creative-publication", "TILT 0006", d="June 18, 2026", s="2026-06-18", venue="Tilted House",
  det=["Placemat Project featuring 4 Visual Pieces - TicTacToe, Connect the Dots, Coloring Sheet, Word Search"],
  links=[("TILT 0006", "https://www.tiltedhouse.org/tilt-0006")])
E("creative-publication", "Fictions “HAUNT” + “CARAVAN”; Poems “Claude Explains a Poem” + “Divining”",
  d="Nov 2025", s="2025-11", venue="Michigan Quarterly Review",
  det=["Fictions in collaboration w/ Computer Scientist John K. Lewis", "Curated by Lillian-Yvonne Bertram"],
  links=[("Michigan Quarterly Review", "https://sites.lsa.umich.edu/mqr/current-issue-fall-2025/")])
E("creative-publication", "“mycelium of my name,” “Apartment,” and “notesapp triptych in which telling the truth gets easier”",
  d="Sept. 2025", s="2025-09", venue="OROBORO Volume 11",
  links=[("Read", "https://deathrattle.org/vol-11-blog/dvvonvhas564zke0n7c10d40iw77jh")])
E("creative-publication", "3 Visual Poems / Text-Artworks", d="June 26, 2025", s="2025-06-26",
  venue="Burning House Press", det=["Curated by Guest Editor John Trefry"],
  links=[("Read", "https://burninghousepress.com/2025/06/26/3-works-by-p-d-edgar/")])
E("creative-publication", "“STONE” and “I Square Myself with my Observable Universe”", d="June 2025",
  s="2025-06", venue="SAND Journal", loc="Berlin", det=["Printed"],
  links=[("SAND Journal Issue 28", "https://sandjournal.com/product/issue-28/")])
E("creative-publication", "“I make a patchwork of my childhood”", d="Jan 1, 2025", s="2025-01-01",
  venue="AI Literary Review", det=["Online"], links=[("Issue 03", "http://ailiteraryreview.co.uk/issue03")])
E("creative-publication", "“Daddy,” “Indifferent Dog,” and “Too much has happened—”", d="June 2023",
  s="2023-06", venue="Dogboy Zine", det=["Printed"])
E("creative-publication", "“A roundabout way of saying ‘Se Busca Asesino’”", d="March 20, 2023",
  s="2023-03-20", venue="Ghost Proposal Issue 13", links=[("Read", "https://ghostproposal.com/PD-Edgar")])
E("creative-publication", "“At least 18 photos of fish”", d="Apr 9, 2022", s="2022-04-09",
  venue="Ekphrastic Review",
  links=[("Read", "https://www.ekphrastic.net/the-ekphrastic-review/at-least-18-photos-of-fish-by-p-d-edgar")])
E("creative-publication", "“Ghazal for Arjeet”", d="2020", s="2020",
  venue="Going Viral, Austin Poets International’s CoronaVirus Anthology",
  links=[("Anthology", "https://www.aipf.org/corona-virus-anthology.html")])
U("Zines")
E("zine", "[Untitled] with Alyssa Barrack on AI / Process/Pedagogy", d="Present", st="in-progress", on=True,
  det=["WIP"])
E("zine", "Unconference Potluck", d="May 2026", s="2026-05",
  det=["Output from Workshop at NMWP Unconference"], links=[("Unconference Potluck", "http://remediatelitmag.xyz/offgrid")])
E("zine", "Notta Zine", d="Apr 2026- Pres.", s="2026-04", on=True,
  det=["Ekphrastic writing zine, ongoing monthly publication in Lakeland, FL"],
  links=[("Notta Gallery", "https://nottagallery.com/")])

# ---------------------------------------------------------------- Conferences, talks, readings
S("Conference Presentations, Invited Talks, & Readings", "Scholarly")
U("In Submission")
E("submission", "Contributors’ Networks by Genre in the Curran Index", st="in-submission",
  venue="Research Society for Victorian Periodicals", det=["Paper Submission"])
dh = [("Digital Humanities 2027 CFP", "https://dh2027.adho.org/cfp/")]
E("submission", "Editing Electronic Literature in the Age of Agentic AI — Creative Care and Contributor Communities",
  d="28 June - 3 July 2027", s="2027-06-28", e="2027-07-03", st="in-submission", grp="dh2027",
  venue="Alliance for Digital Humanities Organizations, Digital Humanities 2027", role="Creativity Short Paper", links=dh)
E("submission", "Virtual Presentation of re•mediate via Zoom", d="Feb. 4, 2027", s="2027-02-04",
  st="in-submission", venue="2027 New Media Caucus Showcase, Elizabeth Foundation for the Arts", loc="NYC",
  det=["Submitted Proposal"], cat="Creative")
U("Conference Presentations")
E("conference-presentation", "E-Lit Periodicals in the Age of AI: Towards More Critical Attention", d="July 2026",
  s="2026-07", venue="Electronic Literature Conference", loc="Online",
  role="Logistics Chair: (Un)Supervised Conference theme/keynotes/scheduling; Panel Organizer")
E("conference-presentation", "Little Networks: Mapping Digital Modernisms", d="July 1-4 2026",
  s="2026-07-01", e="2026-07-04", venue="Modernist Studies Association - Weird Modernisms", loc="Loughborough, UK",
  role="Paper", det=["Part of Panel: “Modernist Poetics and the Digital”"], grp="msa2026")
E("conference-presentation", "Environment Special Interest Group: More-than-human relationalities.",
  d="July 1-4 2026", s="2026-07-01", e="2026-07-04", venue="Modernist Studies Association - Weird Modernisms",
  loc="Loughborough, UK", role="Chair, Paper Panel", grp="msa2026")
E("conference-presentation", "Let Us Cook !! Together in the Text Kitchen", d="May 2026", s="2026-05",
  venue="New Media Writing Prize Unconference", loc="Online", role="Workshop",
  det=["Live Co-Creation of a Zine with a computational interface for text manipulation"])
E("conference-presentation", "Sort, Think, Act: Station-Based AI Literacy Workshops for Students and Professional Development",
  d="Mar 16-17, 2026", s="2026-03-16", e="2026-03-17", venue="Sunshine State Teaching and Learning Conference",
  loc="Orlando, FL", role="Workshop Session", det=["Analog AI Literacy Exercises"], cat="Teaching & Pedagogy")
E("conference-presentation", "Poetry’s Potential Re-Publics: An Archaeology of Latin American Newspaper Poems",
  d="Jan 8-11, 2026", s="2026-01-08", e="2026-01-11", venue="Modern Language Association", loc="Toronto, Canada",
  det=["on Panel “The Technological Turn: Intersections of Technology and Literature in Latin America”"])
E("conference-presentation", "Mise-en-Place: Found Poetry, Computer-Generated Text, and Code as Kitchen Tools",
  d="Nov 7-8, 2025", s="2025-11-07", e="2025-11-08", venue="Creative Writing Studies Conference", loc="Online")
E("conference-presentation", "Process Notes: Editing New CPU- and GPT-Friendly Literary Magazines",
  d="July 10-13, 2025", s="2025-07-10", e="2025-07-13", venue="Electronic Literature Organization",
  loc="Toronto, Canada", det=["Organized collaboration with Dan Power, Katy Gero, and Kyle Booten"])
E("conference-presentation", "Poser, Meme, or Plagiarist: Instapoetry Snark and Gendered Media Genres",
  d="Jun 27-29, 2025", s="2025-06-27", e="2025-06-29", venue="Console-ing Passions", loc="Atlanta, GA")
E("conference-presentation", "Celebrity Poetry: The Literary Multi-Verse of Film and Music Stars",
  d="Apr 16-19, 2025", s="2025-04-16", e="2025-04-19",
  venue="Pop Culture Association / American Culture Association", loc="New Orleans, LA")
E("conference-presentation", "Published and Forthcoming: Computational Approaches to Literary Network Mapping",
  d="Mar 26-27, 2025", s="2025-03-26", e="2025-03-27", venue="UCF Student Scholar Symposium", loc="Orlando, FL")
E("conference-presentation", "Decoding the Black Box: Discerning AI Rhetorics About and Through Poetic Prompting",
  d="Mar 17-20, 2025", s="2025-03-17", e="2025-03-20", venue="IEEE Symposium Series on Computational Intelligence",
  loc="Trondheim, Norway", role="With Alia Hall", det=["Late-Breaking Paper, Poster Presentation"])
E("conference-presentation", "Poetry Contest: Social Media Fandom and Celebrity Poems, Poets, & Poetry",
  d="Dec 2, 2024", s="2024-12-02", venue="DCRG Presents! Day of DH, UCF Center for Humanities and Digital Research")
E("conference-presentation", "“Crisis” as a Catalyzing, Generative Program in Writing Classrooms",
  d="Nov 16-17, 2024", s="2024-11-16", e="2024-11-17", venue="Creative Writing Studies Conference, Virginia Tech",
  loc="Blacksburg, VA", cat="Teaching & Pedagogy")
fcea = [("Florida College English Association", "https://fcea.online")]
E("conference-presentation", "Docupoetics in 360: Experiments in Place-Memory as/in Virtual Reality",
  d="Jan 31-Feb 2 2025", s="2025-01-31", e="2025-02-02", venue="Florida College English Association Conference",
  loc="Ybor City, FL", grp="fcea", links=fcea)
E("conference-presentation", "I Think We’re Getting Slobs: Americentric Bias in The Ugly American",
  d="October 2017", s="2017-10", venue="Florida College English Association Conference", loc="Melbourne, FL",
  grp="fcea", links=fcea)
E("conference-presentation", "ChatGPoeT: Coaching AI & Poetic Forms", d="Sep 11-12, 2024", s="2024-09-11",
  e="2024-09-12", venue="Digitorium - University of Alabama Digital Humanities Conference", loc="Tuscaloosa, AL",
  det=["Delivered virtually"], links=[("Digitorium", "https://adhc.lib.ua.edu/digitorium/")])
E("conference-presentation", "‘The Only Character is an Old Woman, Fiercely Alive’: How Ms. Magazine’s Poetry Shaped What ‘Liberation’ Looked Like",
  d="Feb 4-6, 2023", s="2023-02-04", e="2023-02-06",
  venue="American Journalism Historians Association, Southeast Symposium", loc="Panama City, FL")
fl = "Fiat Lux Undergraduate Research Conference, Florida Southern College"
E("conference-presentation", "Who Lives, Who Dies, Who Tells Your Story? A Literary Analysis of Popularly- Marketed Narratives of U.S. History",
  d="Spring 2019", s="2019-03", venue=fl, grp="fiatlux")
E("conference-presentation", "Frank Lloyd When: Visualizing FSC’s Archived Blueprints", d="Spring 2019",
  s="2019-03", venue=fl, det=["on behalf of M.A.C."], grp="fiatlux")
E("conference-presentation", "On to Avalon: The History of Avalon Groves", d="Spring 2017", s="2017-03",
  venue=fl, det=["on behalf of the McKay Archives Center"], grp="fiatlux")
U("Conducted Workshops", "Teaching & Pedagogy")
E("workshop-conducted", "Sort, Think, Act: Station-Based AI Literacy Workshops for Students and Professional Development",
  d="Mar 16-17, 2026", s="2026-03-16", e="2026-03-17", venue="Sunshine State Teaching and Learning Conference",
  det=["Teacher-oriented workshop with analog approaches to AI Literacy"])
E("workshop-conducted", "AI & Me", d="Nov 21, 2025", s="2025-11-21", venue="Lakeland Christian School",
  loc="Lakeland, FL", det=["6-station AI literacy workshop with 9th & 10th grade students & teachers",
                           "Developed in collaboration with High School Principal Jason Roloff & Annie Bolter, M.A."])
E("workshop-conducted", "How To: Love Poetry", d="Feb 12, 2025", s="2025-02-12",
  venue="Valencia College English Department", role="Zoom Workshops",
  det=["By invitation of instructional librarian Emilie Buckley, Valentines Day poetry exercises"])
E("workshop-conducted", "InDesign & The Creative Writer Studio Sessions", d="Apr. 29 - May 1, 2022",
  s="2022-04-29", e="2022-05-01", venue="University of Alabama", det=[
      "4 sessions", "Three-day demonstration and workshop of Adobe InDesign for creative applications."])
U("Invited Talks")
E("invited-talk", "What can I do with an English degree?", d="Nov 18, 2025", s="2025-11-18",
  venue="Florida State University", role="Class Talk", cat="Teaching & Pedagogy",
  det=["By invitation of instructor Sarah Bliss, virtual discussion of post-undergraduate career with undergraduate students"])
E("invited-talk", "Study, Make, Start, Show", d="Oct 30, 2025", s="2025-10-30",
  venue="University of Central Arkansas", role="Research Talk",
  det=["By invitation of assistant professor Acie Clark, virtual discussion on critical making, AI, and re•mediate lit mag to faculty and MFA students"])
E("invited-talk", "re•mediate Issue•3 Preview & Reading", d="July 8, 2025", s="2025-07-08",
  venue="Electronic Literature Organization: Second Tuesday Salon", det=["with Monica Storss (Guest Editor) on Zoom"],
  cat="Editorial & Publishing")
E("invited-talk", "Short Interactive Presentation on Education, Pedagogy and AI", d="June 10, 2025",
  s="2025-06-10", venue="Lakeland Christian School", loc="Lakeland, FL", cat="Teaching & Pedagogy",
  det=["K-12 In-service day, by invitation of Director of Academics Mike Zavada"])
aspa = [("Alabama Scholastic Press Association", "https://aspa.ua.edu")]
E("invited-talk", "Lit Mags For All: How to Start a Literary Arts Magazine Your Community Reads", d="Feb. 12, 2024",
  s="2024-02-12", venue="Alabama Scholastic Press Association", grp="aspa", links=aspa, cat="Editorial & Publishing",
  det=["Co-Presented with Kate DeLay and Chloe Colbert, co-editors of BWR"])
E("invited-talk", "Lit Mags For All (similar presentation)", d="Feb. 12, 2023", s="2023-02-12",
  venue="Alabama Scholastic Press Association", grp="aspa", links=aspa, cat="Editorial & Publishing",
  det=["Similar presentation, co-presented with Javier Sandoval and Jeremy Rock"])
E("invited-talk", "Lit Mag Reading Club Chat with the Editors of Black Warrior Review", d="Dec. 27, 2023",
  s="2023-12-27", venue="Lit Mag News", cat="Editorial & Publishing",
  links=[("Lit Mag News", "https://litmagnews.substack.com/p/send-the-strangest-thing-you-have")],
  det=["One of two editors interviewed by Becky Tuch, editor of Lit Mag News, on a live-recorded Zoom about literary magazine design"])
E("invited-talk", "Writing Center Tutor Training Week", d="Aug. 14, 2023", s="2023-08-14",
  venue="University of Alabama", cat="Teaching & Pedagogy",
  det=["By invitation of director", "Panel and Q&A with former writing center tutors about tutor-client interactions"])
E("invited-talk", "Lunch and Launch", d="Oct. 13, 2021", s="2021-10-13",
  venue="Florida Southern College Career Services Center", cat="Teaching & Pedagogy",
  det=["By invitation of Jeannie Pond", "Zoom Panel discussion about graduate school applications"])
E("invited-talk", "“Formal Intentions”: Writing in and Inventing Forms of Poetry: Introduction to Concrete and Visual Poetry",
  d="Sep. 24, 2021", s="2021-09-24", venue="EN 508 (3D Poetics Course), University of Alabama",
  cat="Teaching & Pedagogy", det=["By invitation of instructor"])
E("invited-talk", "“Poe-try-pography”: Print History and Digital Practice & Typographic Poetics", d="Sep. 14, 2021",
  s="2021-09-14", venue="EN 200 Intro to Creative Writing Class, University of Alabama",
  cat="Teaching & Pedagogy", det=["By invitation of instructor"])
E("invited-talk", "“A Complex / & Simple / [B]order: [Re]Connecting to Family and Self in a hybrid text”",
  d="Feb. 5, 2020", s="2020-02-05", venue="Speaking of English: Senior Seminar Redux", loc="Lakeland, FL")
U("Programmed Readings of Creative Writing", "Creative")
ob = "Open-Book : A Reading Event for Creative Writers, @ Hillcrest Coffee"
obl = [("Open-Book", "https://www.instagram.com/p/DOUe58bjEzz/")]
E("reading", "Open-Book", d="April 25, 2026", s="2026-04-25", venue=ob, loc="Lakeland, FL", grp="openbook",
  links=obl, det=["Read three poems."])
E("reading", "Open-Book", d="Oct 4, 2025", s="2025-10-04", venue=ob, loc="Lakeland, FL", grp="openbook",
  links=obl, det=["Read three poems titled “BESIDES,”"])
E("reading", "Open-Book", d="March 6, 2025", s="2025-03-06", venue=ob, loc="Lakeland, FL", grp="openbook",
  links=obl, det=["Read three poems."])
E("reading", "Burning House Press’s “Inanimism” Launch Reading", d="June 28, 2025", s="2025-06-28",
  det=["Read pieces of “[1. In January, you hear the winds]” and “TO BE READ WITH TIME”"])
E("reading", "MFA Creative Writing Graduating Student Readings", d="Apr 5 & 7, 2024", s="2024-04-05",
  e="2024-04-07", venue="Sella Granata Gallery, U.Alabama", role="Reader",
  det=["poems and essays from portions of MFA Creative Writing Thesis"],
  links=[("Instagram", "https://www.instagram.com/p/C5V8lteOL8R/")])
E("reading", "Night of the Aesthetes", d="Mar 1, 2024", s="2024-03-01", venue="Sella Granata Gallery, U.Alabama",
  det=["mixed media showcase", "Read poem “Power-dressing, Vogue 2017” & others"],
  links=[("Instagram", "https://www.instagram.com/p/C3aoIKeuM_W/")])
E("reading", "Poets vs. Prose Fall Classic", d="Oct 19, 2023", s="2023-10-19",
  venue="Burrell Odom Park", loc="Tuscaloosa, AL",
  det=["One of three poets invited to read sections of MFA Thesis at public softball game"])
E("reading", "Pure Products Reading @ the Kathryn Tucker Windham Storytelling Tent", d="Oct 14, 2023",
  s="2023-10-14", venue="52nd Annual Kentuck Arts Festival", loc="Northport, Alabama", role="Reader",
  det=["entirety of revised essay “10 Questions to Diagnose your Spiritual Health”"])
E("reading", "Upperclass Student Reading", d="Sept 8, 2023", s="2023-09-08", venue="Ora Mae Gallery",
  loc="Holt, AL", det=["1st Reader in first of three upperclass student readings from UA Creative Writing MFA"],
  links=[("Instagram", "https://www.instagram.com/p/CwvPSeuuqlc/")])
E("reading", "“A Reading of Poetry”", d="Apr 26, 2023", s="2023-04-26", venue="University of Alabama",
  role="Reader", det=["poems “Triptych in Which Telling the Truth Gets Easier” and “Light Green”"],
  links=[("Instagram", "https://www.instagram.com/p/CrdnxBdODVE/")])
E("reading", "Exhibition Opening", d="April 9, 2023", s="2023-04-09", venue="Canterbury Chapel",
  loc="Tuscaloosa, Alabama", role="Reader", det=["poem “A Gathering Up, A Casting”"])
E("reading", "“American Idiots and International Friends”", d="Nov 28, 2022", s="2022-11-28",
  venue="University of Alabama", role="Reader",
  det=["portion of essay “10 Questions to Diagnose Your Spiritual Health”"],
  links=[("Instagram", "https://www.instagram.com/p/ClZpY83ugoj/")])
E("reading", "Documentary Poetics Reading", d="Apr 22, 2021", s="2021-04-22", venue="University of Alabama, Zoom",
  role="Reader", det=["2 sonnet selections from project “A Crown For Spring”"])
E("reading", "Visiting Student Week Current Student Reading", d="Mar 9, 2021", s="2021-03-09",
  venue="University of Alabama, Zoom", role="Reader",
  det=["2 poems: “So Last Year” and “Results, or, I’m sure you have all the answers”"])
E("reading", "First-Year Student Reading Series", d="Nov 2, 2020", s="2020-11-02",
  venue="University of Alabama, Zoom", role="Reader",
  det=["Read 3 poems: “Thoroughway,” “A Roundabout Way,” and “Porch Time”"])
U("Art Shows", "Creative")
E("art-show", "SPACE Invasion", d="March 21, 2026", s="2026-03-21",
  venue="SPACE Collective + Depot Arts District", loc="Lakeland, FL",
  det=["“SEE HERE” - Tabloid Newspaper documentary poetics pieces",
       "“Poetry Placemat” - Interactive take-home poetry paper (200 copies)"])
E("art-show", "Art Night", d="July 1, 2022", s="2022-07-01", venue="Turbo Coffee", loc="Tuscaloosa, AL",
  det=["Read several tabloid-size print, interactive, and digital (360-degree video) documentary poetics pieces at "
       "public “First Friday” gallery showing; print work stayed hung after"])

# ---------------------------------------------------------------- Administrative
S("Administrative Experience", "Organizing & Administration")
U("Logistics Chair, Electronic Literature (Un)supervised Conference 2026")
E("admin-role", "Logistics Chair, Electronic Literature (Un)supervised Conference 2026", d="Fall 2025 - July 2026",
  s="2025-08", e="2026-07", venue="ELO Coordinator + UCF Assistantship Role, Texts & Technology Program, University of Central Florida",
  det=["Planning ELO 2026 Conference Call for submissions + Peer review process",
       "Designing program schedule and proceedings document, video recordings",
       "Coordinating Proceedings, Exhibition, Performances, etc."])
U("Electronic Literature Organization, Coordinator")
E("admin-role", "Electronic Literature Organization, Coordinator", d="Aug 2025–Present", s="2025-08", on=True,
  venue="Assistantship Role in Texts and Technology Program, University of Central Florida",
  det=["Web Management and Digital Communications",
       "Biweekly meetings with ELO President, Occasional attendance ELO Board of Directors Meetings",
       "Membership, Email List Groups, and Query Coordination",
       "Planning ELO 2026 Conference, Designing Forms / Documents, Executing Peer Review Process"])
U("Logistics Chair, Electronic Literature Organization, (Un)linked Conference")
E("admin-role", "Logistics Chair, Electronic Literature Organization, (Un)linked Conference", d="Summer 2024",
  s="2024-06", e="2024-08", venue="Summer Mentoring Fellowship Role, Texts & Technology Program, University of Central Florida",
  det=["Planning ELO 2024 Conference, Designing program and proceedings document, video recordings"])
U("Assistant to the Director of the MFA Program in Creative Writing")
E("admin-role", "Assistant to the Director of the MFA Program in Creative Writing", d="May 2022 – May 2023",
  s="2022-05", e="2023-05", venue="Assistantship Role in Department of English, College of Arts & Sciences, Univ. of Alabama")
U("Events Organizer")
E("event-organized", "Monthly Ekphrastic Writing Workshops", d="April 2026 - present", s="2026-04", on=True,
  venue="Notta Gallery", loc="Lakeland, FL",
  det=["Open-access, free writing events for gallery visitors",
       "Guided writing session with prompts, writing results in Free Notta Zine (now on Issue 6)"])
E("event-organized", "Electronic Literature Conference 2026, (Un)Supervised", d="January - July 2026",
  s="2026-01", e="2026-07", venue="Electronic Literature Organization",
  det=["Logistics Chair, Peer Reviews, Conference Schedule, Proceedings + Recordings",
       "Designed Theme & Brand, Drafted Call for Proposals", "Invited Keynote Speakers"])
rv = "Re•mediate New Issue Launches (Digital Magazine, Zoom)"
E("event-organized", "re•mediate Issue•7 Launch", d="Nov 15, 2026", s="2026-11-15", st="completed", venue=rv,
  grp="launches")
E("event-organized", "re•mediate Issue•5 Launch", d="Apr 18, 2026", s="2026-04-18", venue=rv, grp="launches",
  det=["9 contributors across 7 time zones"])
E("event-organized", "re•mediate Issue•4 Launch, Theme: [MachineWitness]", d="Nov 15, 2025", s="2025-11-15",
  venue=rv, grp="launches", det=["9 contributors across 8 time zones"])
E("event-organized", "re•mediate Issue•3 Launch, Theme: [Next Realities]", d="July 8, 2025", s="2025-07-08",
  venue=rv, grp="launches", det=["10 contributors, co-hosted with Monica Storss"])
E("event-organized", "Electronic Literature Conference 2024, (Un)Linked", d="July 2024", s="2024-07",
  venue="Electronic Literature Organization",
  det=["Logistics Chair, executed proceedings document & program, Recording Team",
       "Member of the Exhibition Committee, curated styles"])
E("event-organized", "Graduating Student Reading Series", d="Apr 2023", s="2023-04",
  venue="University of Alabama @ Sella-Granata Gallery",
  det=["Organizer for 2 readings given by 4 graduating fourth-year MFA students in Poetry"],
  links=[("Instagram", "https://www.instagram.com/p/CrRKSNnueTs/")])
E("event-organized", "Visiting Student Week of Welcome Events", d="Mar 20-23, 2023", s="2023-03-20",
  e="2023-03-23", venue="University of Alabama, Zoom",
  det=["Organized a week of virtual events hosting admitted students to MFA, included: current faculty conferences; "
       "faculty & student readings; topical informational seminars"])
E("event-organized", "“Pride & Joy” Reading", d="Dec 1, 2022", s="2022-12-01", venue="Turbo Coffee Tuscaloosa",
  det=["Organizer for end-of-semester commemoration with Open Mic event, open to public"],
  links=[("Instagram", "https://www.instagram.com/p/CljGUf8OiiR/")])
E("event-organized", "First-Year Reading Series", d="Oct 5, 18, & 25, 2022", s="2022-10-05", e="2022-10-25",
  venue="University of Alabama, Sella Granata Gallery",
  det=["Organizer for 3 readings given by 15 first-year MFA students in Fiction and Poetry"],
  links=[("Instagram", "https://www.instagram.com/p/CkOyyvoOZ_j/")])
E("event-organized", "Second-Year Reading Series", d="Sept 10 & 29, 2022", s="2022-09-10", e="2022-09-29",
  venue="Turbo Coffee Tuscaloosa",
  det=["Organizer for 2 readings given by 8 second-year students in Fiction, Poetry, Nonfiction"],
  links=[("Instagram", "https://www.instagram.com/p/Ci_EBshuYsJ/")])
E("event-organized", "Biannual MFA Clothing Swap & Donation Drive", d="Fall 2022 - Spring 2024", s="2022-08",
  e="2024-05", det=["Every fall semester and spring semester, donations delivered to America’s Thrift"],
  links=[("Instagram", "https://www.instagram.com/p/CpXwu6vueJB/")])
U("Master of Ceremonies")
E("emcee", "Electronic Literature Organization (Un)Linked Conference Performances", d="Jul 19 & 20, 2024",
  s="2024-07-19", e="2024-07-20", det=["Two nights of virtual programming (9 globally-located performances)"])
E("emcee", "Gulf Coast, The Offing, & Black Warrior Review Offsite Reading", d="Mar 10, 2023", s="2023-03-10",
  venue="Ada’s Technical Books", loc="Seattle, WA", det=["portion of event (introduced BWR and its 4 readers)"])
E("emcee", "Puerto Del Sol & Black Warrior Review Launch Reading", d="Mar 25, 2022", s="2022-03-25",
  venue="James Oliver Gallery", loc="Philadelphia, PA", det=["half of event (introduced BWR and its 10 readers)"])

# ---------------------------------------------------------------- Professional Development
S("Professional Development", "Education & Training")
U("Certificate Courses")
E("certificate-course", "Graduate Student Writing Retreat", d="Summer 2026", s="2026-06", e="2026-08",
  venue="UCF Writing Center", det=["Daylong retreat with short workshops"])
E("certificate-course", "“Preparing Tomorrow’s Faculty”", d="Summer 2025", s="2025-06", e="2025-08",
  venue="University of Central Florida Faculty Center for Teaching and Learning",
  det=["12-week course specializing in teaching in higher education"])
U("Creative Workshops Attended")
E("workshop-attended", "Artifeelcial Emotigence", d="August 2025", s="2025-08", venue="UnderAcademy College",
  det=["with Mark Marino and Margaret Rhee"], grp="underacademy")
E("workshop-attended", "Wait List", d="August 2025", s="2025-08", venue="UnderAcademy College", det=["with Talan Memmett and Mark Marino"],
  grp="underacademy")
E("workshop-attended", "Eco-Poetry Workshop", d="Jul 7 –Aug 4, 2024", s="2024-07-07", e="2024-08-04",
  det=["5-week Zoom workshop with Madeline Simms"])

# ---------------------------------------------------------------- Professional Service
S("Professional Service", "Scholarly")
U("Publication Peer Reviews")
E("peer-review", "Creator and Influencer Studies Journal", d="Requested Aug. 28, Submitted Nov. 6, 2026",
  s="2026-08-28", e="2026-11-06", det=["Article Manuscript (Revise & Resubmit)"])
U("Conference Peer Reviews")
E("peer-review", "Electronic Literature Organization 2026 Online Conference", s="2026",
  det=["8 Submissions (4 papers, 1 performance, 1 panel, 2 exhibit items)"])
E("peer-review", "Association for Computers and the Humanities 2026 Conference", s="2026",
  det=["4 Submissions (2 papers, 2 creative submissions)"])
E("peer-review", "Association for Computers and the Humanities 2025 Conference", s="2025",
  det=["3 Submissions (2 papers, 1 creative submission)"])
U("Contests Judged", "Editorial & Publishing")
E("contest-judged", "Florida Undergraduate Humanities Research Journal", d="November 1, 2026", s="2026-11-01",
  det=["6 Essays"], cat="Scholarly")
E("contest-judged", "Jeanne Leiby Memorial Chapbook Award, The Florida Review", d="January-February 2026",
  s="2026-01", e="2026-02", det=["Categories: Prose Chapbook Award, First Reader for 50 submissions (about ¼ of submissions)",
                                "2 of my 5 picks made the Semifinals (Longlist)"])
E("contest-judged", "Alabama Scholastic Press Association Conference", d="Feb 17, 2023", s="2023-02-17",
  venue="U. Alabama", loc="Tuscaloosa",
  det=["Categories: Literary Magazine Overall; Literary Magazine Cover; Lit. Mag. Art; Lit. Mag. Art Portfolio; "
       "Lit. Mag. Photography; Lit. Mag. Poetry; Lit. Mag. Poetry Layout; Lit. Mag. Photography Portfolio; "
       "Lit. Mag. Illustration; Lit. Mag. Short Fiction; Lit. Mag. Creative Nonfiction; "
       "Lit. Mag. Carry-In : Illustration; Lit. Mag. On-site : 3 categories [Fiction / Illustration / Poetry]"])
U("Committees Served", "Organizing & Administration")
E("committee", "MFA Representative, Undergraduate Studies Committee", d="Fall 2022", s="2022-08", e="2022-12",
  venue="English Department, U. of Alabama")

# ---------------------------------------------------------------- Honors
S("Honors, Fellowships & Grants, and Awards", "Recognition & Funding")
U("Media Coverage", "Editorial & Publishing")
H("Of re•mediate, my literary magazine")
E("media-coverage", "What do editors mean when they seek “risk-taking” writing?", d="Dec. 13, 2025",
  s="2025-12-13", venue="Lit Mag News",
  links=[("Read", "https://litmagnews.substack.com/p/q-what-do-editors-mean-when-they")])
E("media-coverage", "FISH List of Lively Literary Magazines", d="Dec. 2025", s="2025-12",
  venue="Fiction on the Web", det=["Re•mediate made the FISH List"],
  links=[("FISH List", "https://www.fictionontheweb.co.uk/p/fish-list.html")])
E("media-coverage", "2-part Interview by Katherine Parrish about re•mediate literary magazine", d="Nov. 2025",
  s="2025-11", venue="Periodicities Blog",
  links=[("Part 1", "https://periodicityjournal.blogspot.com/2025/11/katherine-parrish-conversations-with-pd.html"),
         ("Part 2", "https://periodicityjournal.blogspot.com/2025/11/katherine-parrish-conversations-with-pd_01442627467.html")])
E("media-coverage", "New Lit on the Block : : Re•mediate", d="Jan. 2025", s="2025-01", venue="New Pages",
  det=["Interviews with Lit Mag Listing Sites"],
  links=[("Read", "https://www.newpages.com/blog/magazines/magazine-stand/new-lit-on-the-block-remediate/")])
E("media-coverage", "Editor Interview : Re•mediate lit mag", d="Feb. 2025", s="2025-02", venue="Duotrope",
  det=["Interviews with Lit Mag Listing Sites"],
  links=[("Read", "https://duotrope.com/interview/editor/37607/remediate-lit-mag")])
E("media-coverage", "Lit Mags that Are Vibing So Hard It’ll Make Your Teeth Hurt", venue="Chill Subs",
  det=["Curated Collection"], grp="chillsubs")
E("media-coverage", "5 Mags Who Do Things a Little Differently", venue="Chill Subs", det=["Curated Collection"],
  grp="chillsubs")
U("Pending Grant Applications")
E("grant-pending", "Rhizome Microgrants Program 2026", d="2026", s="2026", st="pending",
  det=["CO-OP Application : Rhizome Prize for “Best Work” and “Best Process Note”"],
  links=[("Rhizome Microgrants 2026", "https://rhizome.org/editorial/2026/oct/26/microgrants-2026/")])
U("Fellowships & Grants Received")
H("Research & Tuition Fellowships")
E("fellowship", "UCF Trustees Doctoral Fellowship", d="2024-2028", s="2024", e="2028", on=True,
  det=["4-years full funding for Ph.D. program."], links=[("Fellows", "https://graduate.ucf.edu/meet-our-fellows/")])
E("fellowship", "UCF Summer Mentoring Fellowship", d="Summer 2024", s="2024-06", e="2024-08",
  det=["Pre-Ph.D. mentorship program."],
  links=[("Fellowship", "https://graduate.ucf.edu/fellowships/#summer-mentoring-fellowship")])
E("fellowship", "U. Alabama Graduate Council Fellowship", d="2020 - 2022", s="2020", e="2022",
  links=[("Fellowships", "https://graduate.ua.edu/applicants/funding/#fellowships")])
E("fellowship", "U. Alabama Truman Capote Fellowship", d="2020 - 2021", s="2020", e="2021")
H("Travel Funding")
E("travel-grant", "Modern Language Association Conference - $400 Graduate Student Convention Grant",
  d="January 2026", s="2026-01")
tt = "Texts & Technology Travel Grants"
E("travel-grant", "$500 to attend Modern Language Association, Toronto, Canada", d="January 2026", s="2026-01",
  venue=tt, grp="tt-travel")
E("travel-grant", "$660 to attend Electronic Literature Organization, Toronto, Canada", d="July 2025", s="2025-07",
  venue=tt, grp="tt-travel")
E("travel-grant", "$500+ to attend IEEE Symposium on Computational Intelligence, Trondheim, Norway",
  d="March 2025", s="2025-03", venue=tt, grp="tt-travel")
E("travel-grant", "$500 to attend Creative Writing Studies Conference, Blacksburg, VA", d="November 2024",
  s="2024-11", venue=tt, grp="tt-travel")
E("travel-grant", "UCF Student Government Travel Awards - $1,000 to Attend IEEE SSCI, Trondheim Norway",
  d="March 2025", s="2025-03")
pf = "Presentation Fellowship, UCF Graduate School"
E("travel-grant", "$500 to attend Modern Language Association Conference, Toronto, Canada", d="January 2026",
  s="2026-01", venue=pf, grp="pres-fellowship")
E("travel-grant", "$300 to attend Florida College English Association Conference, Ybor City, FL",
  d="January 2025", s="2025-01", venue=pf, grp="pres-fellowship")
E("travel-grant", "Creative Writing Studies Conference - $400 Graduate Student Travel Stipend")
ua = "U. Alabama Graduate School Conference and Research Funding"
E("travel-grant", "$534 Travel to Granada, Nicaragua, for creative writing thesis research", d="Summer 2023",
  s="2023-06", e="2023-08", venue=ua, grp="ua-funding")
E("travel-grant", "$385 Travel to attend Journalism Historians Association SE Conference, Panama City, FL",
  d="2023", s="2023", venue=ua, grp="ua-funding")
U("Awards Received")
E("award", "Outstanding Journalism Thesis by a Graduate Student", d="April 6, 2024", s="2024-04-06",
  venue="Honors Day, UA School of Communication and Information Sciences, U. of Alabama")
E("award", "Outstanding Creativity in Print Design", d="April 19, 2023", s="2023-04-19",
  venue="Student Media Oscar Awards for Outstanding Student Creativity & Responsibility, U. of Alabama")
E("award", "3rd Place Graduate Paper", d="Feb. 5, 2023", s="2023-02-05",
  venue="American Journalism Historians Association, Southeast Symposium", loc="Panama City, FL")
E("award", "Finalist for the Ultraslant Prize", d="August 15, 2022", s="2022-08-15",
  venue="Ghost Proposal, Digital Literary Magazine", links=[("Ultraslant", "https://ghostproposal.com/ultraslant")])
E("award", "Fulbright Program Semi-Finalist", d="January 2020", s="2020-01")
fsc = "Florida Southern College"
E("award", "Joe P. Ruthven Award for Leadership, Graduation Award", d="Spring 2020", s="2020-04", venue=fsc, grp="fsc-awards")
E("award", "Outstanding English Senior, Modern Language Department", d="Spring 2020", s="2020-04", venue=fsc, grp="fsc-awards")
E("award", "James C. Rogers Outstanding Male Senior Award, Student Gov. Assoc.", d="Spring 2020", s="2020-04", venue=fsc, grp="fsc-awards")
E("award", "Student Life Awards, Diversity Initiative of the Year (Awarded with event co-organizers)",
  d="Apr. 2019", s="2019-04", venue=fsc, grp="fsc-awards")
E("award", "Admissions Department: Southern Ambassadors Rising Star", d="April 7, 2019", s="2019-04-07",
  venue=fsc, grp="fsc-awards")
E("award", "Carroll and Lucy Teeter Journalism Award", d="Spring 2018", s="2018-03",
  venue="Florida Southern College Communications Department", grp="fsc-awards")
E("award", "Eagle Scout Rank", d="May 2016", s="2016-05", venue="Boy Scouts of America")

# ---------------------------------------------------------------- Affiliations
S("Affiliations", "Scholarly")
U("Professional / Academic Organizations")
E("membership", "Creative Writing Studies Organization", d="Yearly Membership Initiated Sept 2024", s="2024-09", on=True)
E("membership", "Florida Digital Humanities Consortium", d="Yearly Membership Initiated May 2024", s="2024-05", on=True)
E("membership", "Electronic Literature Organization", d="Yearly Membership Initiated May 2024", s="2024-05", on=True)
U("Honor Societies", "Recognition & Funding")
H("Inducted April 20, 2023 at The University of Alabama")
E("honor-society", "Kappa Tau Alpha, National Journalism and Mass Communication Honor Society",
  d="April 20, 2023", s="2023-04-20", venue="The University of Alabama")
H("Inducted at Florida Southern College, 2017-2019")
for t in ["Lambda Pi Eta, Omega Iota Chapter, International Communications Honor Society",
          "Omicron Delta Kappa, Florida Southern College Circle, International Honor Society",
          "Sigma Tau Delta, Psi Epsilon Chapter, International English Honor Society"]:
    E("honor-society", t, d="2017-2019", s="2017", e="2019", venue="Florida Southern College", grp="fsc-honor")

# ---------------------------------------------------------------- Skills
S("Skills", "Work & Skills")
U("Languages")
E("skill", "Fluent in English, Spanish", det=["English", "Spanish"])
E("skill", "Learner in html, CSS, Python, Twine", det=["html", "CSS", "Python", "Twine"])
U("Software")
E("skill", "Professional/Artistic Experience", det=[
    "Adobe InDesign", "Express", "Google Drive / Suite", "Wordpress", "Readymag", "Buffer", "Instagram",
    "Claude Code", "ChatGPT", "Google Gemini", "BlueSky", "Python", "HTML", "CSS", "Bitly", "Twine"])
E("skill", "Proficient", det=["Twitter/X", "LinkedIn", "Snapchat", "BeReal", "Facebook", "Microsoft Suite",
                              "Google Suite", "Zotero"])
E("skill", "Knowledgeable", det=["Adobe Audition", "Premiere Pro", "Photoshop", "Microsoft Excel", "Hootsuite",
                                 "Buffer", "Editorial Manager"])
# ---------------------------------------------------------------- Conference Attendance (was an H2 under Skills)
S("Conference Attendance", "Scholarly")
U(None)
def A(title, d, s, e=None, loc=None, grp=None, st=None):
    E("conference-attendance", title, d=d, s=s, e=e, loc=loc, grp=grp, st=st)
A("Modern Language Association", "Jan. 9-11, 2026", "2026-01-09", "2026-01-11", "Toronto, Ontario, Canada")
A("Latin America and Caribbean Digital Humanities Conference", "Nov. 12-14, 2025", "2025-11-12", "2025-11-14",
  "Online Conference Track, hosted by University of Florida")
A("Creative Writing Studies Organization Conference", "November 7-8, 2025", "2025-11-07", "2025-11-08",
  "Online Conference: “Relatable!”", "cwso")
A("Creative Writing Studies Organization Conference", "Nov. 16-17, 2024", "2024-11-16", "2024-11-17",
  "Blacksburg, VA, hosted by Virginia Tech", "cwso")
A("Electronic Literature Conference", "July 2026", "2026-07", None,
  "Virtual Conference, hosted by University of Central Florida", "elc")
A("Electronic Literature Conference", "July 10-13, 2025", "2025-07-10", "2025-07-13",
  "Toronto, Ontario, Canada, hosted by University of York, University of Waterloo", "elc")
A("Electronic Literature Conference", "July 18-21, 2024", "2024-07-18", "2024-07-21",
  "Virtual Conference, hosted by University of Central Florida", "elc")
A("Console-ing Passions", "June 27-29, 2025", "2025-06-27", "2025-06-29",
  "Virtual Attendance, hosted by Georgia State University")
A("The Association for Computers and the Humanities", "June 24-26, 2026", "2026-06-24", "2026-06-26",
  "Virtual Conference", "ach")
A("The Association for Computers and the Humanities", "June 11-13, 2025", "2025-06-11", "2025-06-13",
  "Virtual Conference", "ach")
A("New Media Writing Prize Unconference", "May 12-13, 2026", "2026-05-12", "2026-05-13", "Virtual Conference", "nmwp")
A("New Media Writing Prize Unconference", "May 13-14, 2025", "2025-05-13", "2025-05-14", "Virtual Conference", "nmwp")
A("Pop Culture Association/American Culture Association", "Apr. 16-19, 2025", "2025-04-16", "2025-04-19",
  "New Orleans, LA")
A("UCF Student Scholar Symposium", "March 26-27, 2025", "2025-03-26", "2025-03-27", "Orlando, FL")
A("IEEE Symposium Series on Computational Intelligence", "March 17-20, 2025", "2025-03-17", "2025-03-20",
  "Trondheim, Norway")
A("Florida College English Association Conference", "Jan 31-Feb 2, 2025", "2025-01-31", "2025-02-02",
  "Ybor City, FL", "fcea-att")
A("Florida College English Association Conference", "Oct 19-21, 2017", "2017-10-19", "2017-10-21",
  "Melbourne, FL", "fcea-att")
A("Florida Digital Humanities Consortium", "Sep 19-20, 2024", "2024-09-19", "2024-09-20",
  "Orlando, FL, hosted at University of Central Florida")
A("Digitorium: University of Alabama Digital Humanities Conference", "Sep 11-12, 2024", "2024-09-11",
  "2024-09-12", "Virtual attendance, hosted at University of Alabama")
A("American Journalism Historians Association Southeast Symposium", "Feb 4-6, 2023", "2023-02-04",
  "2023-02-06", "Panama City, FL")
for d_, s_, e_, l_ in [("Feb 7-10, 2024", "2024-02-07", "2024-02-10", "Kansas City, Missouri"),
                       ("Mar 8-11, 2023", "2023-03-08", "2023-03-11", "Seattle, Washington"),
                       ("Mar 23-26, 2022", "2022-03-23", "2022-03-26", "Philadelphia, Pennsylvania"),
                       ("Mar 3-7, 2021", "2021-03-03", "2021-03-07", "Virtual Attendance from Tuscaloosa, AL")]:
    A("Association of Writers and Writing Programs Conference", d_, s_, e_, l_, "awp")
A("Diversity and Inclusion Conference, Still We Rise: Resilience in Social Experiences", "Feb 1, 2020",
  "2020-02-01", None, "University of South Florida St. Petersburg; St. Petersburg, FL (Inaugural)")
A("Association of Student Government Associations", "Oct 10-13, 2019", "2019-10-10", "2019-10-13", "Washington, D.C.")
A("College Media Association Conference", "Oct 31-Nov 3, 2019", "2019-10-31", "2019-11-03", "Washington, D.C.", "cma")
A("College Media Association Conference", "Oct 24-Oct 27, 2018", "2018-10-24", "2018-10-27", "Louisville, KY", "cma")

# ---------------------------------------------------------------- Freelance
S("Freelance Work Experience", "Work & Skills")
U("Substitute Teacher, Upper Schools, Lakeland, FL", "Teaching & Pedagogy")
E("freelance", "Substitute Teacher, Upper Schools", loc="Lakeland, FL",
  det=["English, Video Production, Songwriting, Geometry, Religious Studies, Boys’ PE, Advisory"])
U("Print Layout Design, Publications & Creative Projects", "Editorial & Publishing")
E("freelance", "Manuscript Layout W. artist Kalie Boyne", det=["to print graphic novel My World Belongs To Me"],
  links=[("Kalie Boyne books", "https://www.kalieboyne.com/books")])
E("freelance", "Manuscript Layout W. poet Kwoya Fagin Maples", det=["to lay out section of poetry manuscript"],
  links=[("Link", "https://www.kalieboyne.com/books")])
E("freelance", "Illustrated Map Design W. nonfiction writer Kathryn Fitzpatrick’s manuscript",
  det=["hand-drawn map of CT"])
E("freelance", "Chapbook Layout W. poet Marzetta", det=["to layout design print book collection The Garden"],
  links=[("The Garden", "https://www.amazon.com/Garden-Marzetta-ebook/dp/B0B5KTK9BP")])
E("freelance", "Poetry Commission", det=["For Fiverr clients, formatted lines of poetry into concrete shapes"])
U("Copy Editing, Higher Education Admissions/Activities (Names Abbreviated for Privacy)", "Editorial & Publishing")
for t, d_, s_, e_, r in [
        ("Be.Zi. - Dental School Applications", "Spring 2025", "2025-01", "2025-05", "admitted"),
        ("As.Ti. - Medical School Applications & Secondaries", "June-August 2024", "2024-06", "2024-08", "accepted offer"),
        ("Ar.Ti. - Dental School Graduation Speech", "May 2024", "2024-05", None, "delivered"),
        ("Ca.Th. - Law School Applications", "2023 Cycle", "2023", None, "admitted & waitlisted, accepted offer"),
        ("Ca.Th. - Law School Applications", "2022 Cycle", "2022", None, "admitted & waitlisted, deferred admission"),
        ("Ca.Wh. - Master’s Program Application", "2023 Cycle", "2023", None, "admitted, deferred admission"),
        ("Ma.Ga. - P.T. School Applications", "2022 Cycle", "2022", None, "admitted to two schools"),
        ("Sp.As. - Medical School Applications", "2021 Cycle", "2021", None, "admitted"),
        ("Mo.Mc. - Fulbright ETA Application", "", None, None, "awarded upon later submission"),
        ("Ar.Ti. - Dental School Applications", "2019 Cycle", "2019", None, "admitted to two schools")]:
    E("freelance", t, d=d_, s=s_, e=e_, det=[f"Outcome: {r}"])

# ---------------------------------------------------------------- External Work
S("External Work Experience", "Work & Skills")
U("Turbo Coffee Tuscaloosa, Tuscaloosa, AL")
E("employment", "Barista, part-time", d="May 2022- 2024", s="2022-05", e="2024", venue="Turbo Coffee Tuscaloosa",
  loc="Tuscaloosa, AL")
U("Admissions Department, Florida Southern College, Lakeland, FL")
E("employment", "Southern Ambassador (Tour Guide)", d="Spr. 2018 - Spr. 2020", s="2018-01", e="2020-05",
  venue="Admissions Department, Florida Southern College")
E("employment", "Scholars Weekend Leader", d="Jan. 2019", s="2019-01", grp="scholars",
  venue="Admissions Department, Florida Southern College")
E("employment", "Scholars Weekend Leader", d="Jan. 2020", s="2020-01", grp="scholars",
  venue="Admissions Department, Florida Southern College")
U("Sarah D. and L. Kirk McKay Archives Center")
E("employment", "Student Archivist", d="Spr. 2017 - Fall 2019", s="2017-01", e="2019-12",
  venue="Sarah D. and L. Kirk McKay Archives Center")
U("Camp Gilead, Polk City, FL")
for d_, r in [("Summer 2021", "Directors’ Assistant, Head Counselor, Head Lifeguard"),
              ("Summer 2020", "Head Lifeguard, Summer Staff"),
              ("Summer 2019", "Head Counselor, Head Lifeguard"),
              ("Summer 2017", "Senior Counselor, Lifeguard")]:
    y = d_[-4:]
    E("employment", r, d=d_, s=f"{y}-06", e=f"{y}-08", venue="Camp Gilead", loc="Polk City, FL", grp="gilead")

# ---------------------------------------------------------------- Coursework
S("Relevant Coursework to Date", "Education & Training")
U("Doctoral Coursework")
E("coursework", "Ph.D. in Texts & Technology", det=[
    "Introduction to Texts & Technology", "Research Methods in Text & Technology", "History of Texts & Technology",
    "Theories of Texts & Technology", "Dissertation Design", "Media Aesthetics", "Playable Texts & Technology",
    "Interdisciplinary Teaching", "Comprehensive Exams (Passed!)", "Dissertation Hours (Summer 2026 - Graduation)"])
E("coursework", "Digital Humanities in the Age of AI Certificate", det=[
    "Humanities in the Age of AI", "Critical Making in the Age of AI", "Digital Ethics",
    "Social Media Research Methods", "Interdisciplinary Teaching"])
U("Graduate Coursework")
E("coursework", "MFA Creative Writing", det=[
    "Poetry Workshops (3)", "Workshop in Book Arts", "Nonfiction Workshop", "Sem. in 20th Cent.",
    "Am. Lit - Faulkner’s B-Sides", "3D Poetics", "Literary Criticism - Translation", "Documentary Poetics",
    "The Art of the Poetry Reading", "Writing Habits & Process", "Methods in Teaching English as Second Language",
    "Experimental, Hybrid Memoir", "Thesis Hours (6)", "The Case for Poetry", "Pedagogy for Teaching EN [101/102/200]"])
E("coursework", "MA Journalism & Media Studies", det=[
    "Seminar in Communication Theory", "Humanistic Research Methods", "Advanced Magazine Writing",
    "PhD-level Seminar in Visual Rhetorics", "History of Journalism & Media", "Thesis Hours (9)",
    "Contemporary Issues in Journalism (Ethics)"])
U("Undergraduate Coursework, BA")
E("coursework", "English : Writing", det=[
    "Writing for Business", "American Literature I & II (Pre- & Post-1800)", "Rhetoric & Writing",
    "English Literature I & II (Pre- & Post-American Civil War)", "Nonfiction Workshop",
    "Jane Austen (course + study abroad/Junior Journey)", "Senior Seminar", "Multiethnic American Literature",
    "Intro English Studies (Literary Criticism)", "World Literature"])
E("coursework", "Spanish", det=[
    "Summer Intern @ Proyecto Español, language school in Alicante, Spain", "Spanish American Literature",
    "Spanish-Language Literature", "Latin American Film & Fiction", "Spanish Capstone Project"])
E("coursework", "Communications : Multimedia Journalism", det=[
    "News Media Projects", "Internship w. LkldNow", "Online Media", "Intercultural Communication",
    "Communication Law & Ethics", "Mass Media & Society", "Media Writing", "Communications Research",
    "News & Feature Writing", "Desktop Publishing", "Broadcast Journalism", "Professional Development"])

# ---------------------------------------------------------------- vocabularies + write
D["types"] = sorted({x["type"] for x in D["entries"]})
D["categories"] = sorted({x["category"] for x in D["entries"]})
for sec in D["sections"]:
    sec["count"] = sum(1 for x in D["entries"] if x["section"] == sec["id"])

if __name__ == "__main__":
    with open("cv.json", "w", encoding="utf-8") as f:
        json.dump(D, f, ensure_ascii=False, indent=2)
    print(len(D["sections"]), "sections,", len(D["entries"]), "entries,",
          len(D["types"]), "types,", len(D["categories"]), "categories")
    for s in D["sections"]:
        print(f'  {s["order"]:>2}. {s["title"]} ({s["count"]})')
