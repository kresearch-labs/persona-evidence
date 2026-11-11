# Villisca Axe Murders (June 9–10, 1912) — Timeline Research Notes

Investigation subagent notes, compiled 2026-10-19.
Method: every quote below was copied from a page/text actually fetched during this session.
CONTEMPORARY = 1912–1917 newspaper text (OCR); SECONDARY = later/overview sources fetched in full;
SNIPPET-ONLY = seen only in a search-result description.
OCR convention: soft hyphenations at line-ends are joined ("ap­peared" → "appeared"); obvious
OCR misreads inside a copied sentence are preserved and marked [sic] in claim text where material.

## Primary source pipeline (what worked)

- Chronicling America (LOC): search API returns 404 (endpoint retired at chroniclingamerica.loc.gov)
  and page/OCR URLs return 403 (Cloudflare) to urllib; www.loc.gov shows an unsolved Cloudflare
  interstitial in the automation browser. => logged under Inaccessible sources.
- Workaround that DID work: The Villisca Public Library digital archive (Advantage Archives),
  https://villisca.advantage-preservation.com/ — full run of The Villisca Review 1878–2003.
  Issue-page viewer URLs have the form
  https://villisca.advantage-preservation.com/viewer/?fn=the_villisca_review_usa_iowa_villisca_<YYYYMMDD>_english_<seq>
  each page exposes a `GetPdfFile?<PubdateId>` ABBYY-OCR'd PDF; `pdftotext -raw` reconstructs
  correct column reading order. Downloaded page PDFs+text:
  - 1912-06-13 pp.1–8  (first post-murder issue: discovery, scene, inquest day 1)
  - 1912-06-20 pp.1–8  (coroner resumes, reward fund, detectives)
  - 1912-09-12 p.1, 1912-10-24 p.1, 1912-12-19 p.1 (Burns agency; grand juries)
  - 1917-05-16 p.4, 1917-05-19 p.2 (Kelly indictment/self-surrender)
  - 1917-09-05, 1917-09-19, 1917-09-22, 1917-09-29 (first trial)
  - 1917-10-03 p.1 (hung jury), 1917-11-21, 1917-11-24, 1917-11-28 (second trial, verdict)
- Secondary sources fetched in full: Wikipedia, Iowa Cold Cases, Iowa Legislature "Pieces of
  Iowa's Past" PDF (May 13, 2015), murderhouse.com suspects page, Smithsonian Magazine.

## Timeline of verified claims

### The evening of June 9, 1912
1. [CONTEMPORARY] The Moores attended the Presbyterian church; the children "had taken prominent
   parts in the Children's Day exercises" the evening before their death. (Review 1912-06-13 p.8,
   Josiah Moore obituary/bio.)
2. [SECONDARY] Program ended 9:30 p.m.; family + Stillinger girls walked home, arriving 9:45–10 p.m.
   (Wikipedia; same wording in Iowa Legislature PDF.)
3. [CONTEMPORARY] Neighbor P.D. Minick later testified (2nd Kelly trial, 1917) "he saw the Moores
   leave for church" that evening. (Review 1917-11-24 p.3.)
4. [CONTEMPORARY] Rev. Kelly had been in town for the Children's Day services (he came to Villisca
   June 8, 1912 per secondary sources; contemporaneous trial coverage places him in Villisca the
   evening of June 9, taking supper at E.H. Landers' restaurant between 7 and 8, leaving "after
   taking supper" with Landers; Landers' departure time became a trial battleground — Poston swore
   Landers stayed until nearly 10:30, Landers swore he left about 9). (Review 1917-09-22 p.2,
   1917-11-24 p.3.)

### Discovery, Monday June 10, 1912
5. [CONTEMPORARY] "In such condition was the house found at about half past eight o'clock Monday
   morning by Ross R. Moore and Mrs. Mary E. Peckham, who were first to enter and to look upon the
   terrible scene, so far as the downstairs portion of the house contributed to it."
   (Review 1912-06-13 p.1.) NOTE: this contradicts the widely repeated 7:00–7:30 a.m. discovery
   time in later accounts.
6. [CONTEMPORARY — Peckham's sworn inquest testimony] She lived "just next door west of them on
   East Third street"; the two houses "not more than twenty feet" apart; she saw the family before
   church time but not afterwards; she "retired about eight o'clock, not feeling well, and arose
   Monday morning between four and five o'clock" [OCR: "between Hour and f\ye o'clock"]; toward
   eight o'clock she felt a "terrible stillness," noticed all curtains down, went over, knocked and
   found the door locked; horses restless, chickens cheeping, cow unmilked; "Mrs. Peckham returned
   home and called up Ross Moore's residence, and asked Mrs. Moore if there was anything the matter
   down to the C. C. Moore home, or if Father Moore was sick." (Review 1912-06-13 p.1.)
7. [CONTEMPORARY] Ed Selley, an employe of J.B. Moore at the store, was called by Peckham; she
   "asked him" [to come]. (Review 1912-06-13 p.1; Selley's name also on the reward subscription
   list, Review 1912-06-20 p.6.)
8. [CONTEMPORARY] Marshal J.H. Horton "testified to having been called about half past eight
   Monday morning, and of going to the J. B. Moore home and making an examination, revealing the
   awful crime. He took Dr. Cooper with him, and Dr. E. C. Hough joined them on the way to the
   house." (Review 1912-06-13 p.8.)
9. [CONTEMPORARY] "Not until Marshal J. H. Horton appeared upon the scene did any one attempt to
   go upstairs, and then the marshal, in company with Dr. J. C. Cooper and Dr. E. C. Hough, came
   upon the fullness of the awful tragedy." (Review 1912-06-13 p.1.) — i.e., Horton (not Ross
   Moore) was first upstairs; downstairs (the Stillinger girls) was all Ross/Peckham saw.
10. [SECONDARY] Wikipedia/Iowa Legislature PDF version: Peckham noticed undone chores ~7 a.m.,
    knocked, door locked, let the chickens out, called Ross Moore; Ross unlocked the front door
    "with his copy of the house key," found the Stillinger girls, told Peckham to call Hank
    Horton. (Consistent in cast; different clock times.)
11. [CONTEMPORARY] Crowd/crowd contamination: "it is estimated that fully five thousand people
    gathered on the streets of the city Monday, hundreds coming from out of town"; "Poses were
    formed every hour of the day; armed men scoured the country for many miles all day Monday and
    most of Tuesday." (Review 1912-06-13 p.1.)
12. [CONTEMPORARY] Militia: "Company F under Capt. C. J. Casey was ordered out by Sheriff O. E.
    Jackson, and a patrol was stationed around the J. B. Moore home at six o'clock Monday evening
    to keep the curious crowds away until the dogs came to do their work." (Review 1912-06-13
    p.1.) — Guard posted Monday 6 p.m., not at dawn; and it was the sheriff, not the coroner,
    who called it out. The city "has been under martial law since."
13. [SECONDARY] Telephone "all call" ~8:40 a.m. advising every household; townspeople crowded in
    within minutes, contaminating the scene; some "stealing pieces of Josiah's skull as souvenirs";
    murder weapon "handled by hundreds." (Wikipedia.)
14. [SECONDARY] Smithsonian: as many as 100 curious neighbors tramped through the house, one
    removing skull fragments; a local druggist-photographer was dismissed — photos "too ghoulish";
    Dr. F.S. Williams emerged saying "Don't go in there, boys; you'll regret it until the last day
    of your life." (Smithsonian, "The Ax Murderer Who Got Away," June 2012.)
15. [CONTEMPORARY] Bodies removed: "The bodies of the eight were removed from the J. B. Moore home
    Monday night after midnight with Undertakers J. L. Smith and C. N. Fessler of Villisca in
    charge," assisted by A.B. Wolfe, L.V. Myers and Sons, Myron Smith (Red Oak), Walter Sellergren
    (Stanton); during the Wednesday services the bodies lay in caskets at the city hall, "at no
    time were they exposed to the public view." (Review 1912-06-13 p.6.)
16. [CONTEMPORARY] Funeral: "Funeral services for the eight victims of the murderer's ax were held
    in the open air in the public park at Villisca Wednesday afternoon, June 12, 1912, at three
    o'clock." (Review 1912-06-13 p.6.) [SECONDARY: cortege 50 carriages long; National Guardsmen
    blocked the street; burial at Villisca Cemetery — Iowa Legislature PDF / Iowa Cold Cases.]

### Crime scene as reported contemporaneously (June 13, 1912 issue)
17. [CONTEMPORARY] Bodies: Stillinger girls downstairs "in a bed in the northwest room... their
    heads chopped open with an ax"; Moores upstairs north bedroom "on their backs, apparently as
    they were when asleep"; four children "in the south room, in three beds." (Review p.1.)
18. [CONTEMPORARY] Defensive wound: "There were no signs of a struggle on the part of any of the
    victims, except perhaps in the case of one of the girls downstairs, on whose arm a slight cut
    appeared." (Review p.1.)
19. [CONTEMPORARY] Faces covered after the crime "either with part of the bedding or some discarded
    wearing apparel"; "he had taken the precaution to pull down all the window curtains and to
    darken the doors, using an old black apron in one case and a black skirt in the other."
    (Review p.1.) (Mirror-covering per Wikipedia/Smithsonian; the Review documents the curtain/
    door darkening, and the June 20 issue confirms windows darkened upstairs and down; mirrors
    draped per 1917 trial summary: "Even the mirrors in the house had been draped to shut out the
    view of human butchery." Review 1917-09-29 p.2.)
20. [CONTEMPORARY] Doors/windows: "Every door and window was locked except the two windows in the
    room occupied by the Stillinger girls downstairs," and evidence (cobweb + dead fly on one sill,
    sewing machine piled with clothing before the other, undisturbed flower pots) showed the
    windows "had not been used either in entering or leaving"; front dining-room door was locked
    but its key missing — "the only solution of the problem of exit lies in the theory that the
    murderer escaped through the front door, locking it after him and taking the key with him."
    (Review 1912-06-13 p.1.) — This CONTRADICTS later "unlocked back door / no forced entry
    because killer walked in" reconstructions.
21. [CONTEMPORARY] Robbery excluded; money/checks in Moore's trousers on the bedpost: "Robbery was
    not the motive, for nothing is known to have been taken from the place. Mr. Moore's trousers
    hung on the bedpost, and in them were a bunch of keys, three memorandum books, a check drawn
    by his brother, G. A. Moore, and some money. His watch lay on the dresser downstairs in the
    room occupied by the Stillinger girls." (Review 1912-06-13 p.1.)
22. [CONTEMPORARY] Lamp: Kansas City Post reporter M.H. Hobin, "upon receiving a special permit to
    enter the Moore home here, found the missing globe from the lamp which sat on the floor in the
    downstairs bedroom. Finger prints on the globe will be used as a means of identification; as
    will those on the ax found leaning against the wall close to the lamp." (Review 1912-06-13
    p.1.) [SECONDARY adds: wick bent, chimney under a chair/dresser; "imprint in the hay in the
    barn next to a knothole"; two spent cigarettes in the attic; keychain fragment not belonging
    to the Moores — all Wikipedia/Smithsonian.]
23. [CONTEMPORARY] Bloodhounds (Elmer Noffsinger, Beatrice, Neb.): "allowed to scent the ax handle
    and started upon the trail of the murderer... They left by the front door of the house, went
    off the east end of the porch, and up Sixth avenue north to Second street... There they turned
    south and continued straight to Jonas Green's farm on West and Middle Nodaway" — trail lost at
    the river. (Review 1912-06-13 p.1.)
24. [CONTEMPORARY] Time-of-death window data point: "Mrs. F. F. Jones thought she heard a peculiar
    noise in the vicinity of her home, and had Mr. Jones get up and turn on the light. This was
    between one and two o'clock." Also the December 27, 1912 lead-in: dogs' trail ~18–20 hours
    old by Monday night. (Review 1912-06-13 p.1.) [SECONDARY: "Doctors estimated that the murders
    occurred between midnight and 2 a.m." (Wikipedia); "between midnight and 5 a.m." (Iowa
    Legislature PDF).]
25. [CONTEMPORARY] Victims and exact ages (obituary arithmetic): J.B. Moore born Hanover, Ill.,
    Dec 29, 1868 ("forty-three years, five months, and eleven days old when he came to his death");
    Sarah b. Apr 17, 1873; Herman b. Sept 2, 1900 ("eleven years, nine months and eight days");
    Katherine b. Jan 27, 1902; Boyd b. Mar 22, 1905; Paul b. Jan 13, 1907 ("five years, four months
    and twenty-seven days"). Lena Gertrude Stillinger b. [Nov] 1, 1900, "eleven years [X] months
    and nine days old"; Ina May b. [June] 30, 1903, "eight years [X] months and ten days old."
    (Review 1912-06-13 p.8.) NOTE: contemporaneous age for Lena = 11; several later sources say 12.

### Inquest and investigation
26. [CONTEMPORARY] "County Coroner A. L. Linquist of Stanton... began an inquest with a jury of
    three men Tuesday afternoon at half past one o'clock at the city hall, and by half past three
    had examined eleven witnesses... The coroner's jury is composed of Dr. W. A. [L]omas, W. R.
    Finlayson and J. Y. Wickersham," official stenographer J.M. Johnson (Council Bluffs),
    examination conducted by County Attorney W.C. Ratcliff and Coroner Linquist. (Review
    1912-06-13 p.1.) NOTE: coroner = A. L. Linquist — the prompt's "Dr. J.C. Linnas" is wrong;
    Dr. J.C. Cooper was a local physician who went upstairs with Horton.
27. [CONTEMPORARY] Inquest resumed: "Coroner A. L. Linquist and his jury... resumed the taking of
    evidence in the inquest following the tragedy of Sunday night, June 9, on Tuesday forenoon of
    this week [June 18], and three new witnesses were examined... Jury Has Verdict Ready." Key new
    testimony: J.T. Stillinger recalled, described a boarder "Martin Luther Kellum" who worked for
    him May 15–18, 1912, nervous, anxious for his mail, paid by a $5.25 check payable to Ed
    Sandell. (Review 1912-06-20 p.8.)
28. [CONTEMPORARY] First-witness inquest testimony also included Fen Moore, Dr. F.S. Williams,
    J.H. Horton, Lee Van Gilder et al. (Review 1912-06-13 p.8.)
29. [CONTEMPORARY] Reward fund: over $1,000 subscribed at the Villisca National Bank; "This reward
    is to hold good only if capture is made within six months from date, June 11th, 1912."
    (Review 1912-06-20 p.6.)
30. [CONTEMPORARY] Finger-print expert M.W. McClaughry (Leavenworth) summoned by Ratcliff;
    "expresses the opinion that it was some one thoroughly familiar with the premises, and that
    the two girls downstairs were killed first"; "Photographs of the murderer's ax, and of the
    lamp chimney found under the dresser downstairs, were taken at Mr. McClaughry's request... but
    the prints were not conspicuous enough to be photographed very satisfactorily." Dan O'Leary
    (John Hayes agency, hired by the county), L.W. Longnecker (Omaha, hired by citizens) continue;
    Pinkerton man "Gillson" (Kansas City) investigated unpaid; Burlington special agent J.M.
    Harrison and W.D. Griffin (president, state sheriffs' association) arrived Thursday June 13.
    (Review 1912-06-20 p.4.)
31. [CONTEMPORARY] State/Burns: "According to information which comes from Des Moines, Attorney
    General Cosson has again employed a member of the Burns detective agency on the Villisca murder
    case. The man is W. S. Gordon of Kansas City, and he succeeds C. W. Tobie, who first
    investigated the case but was subsequently transferred to the Chicago agency. Mr. Gordon and
    County Attorney W. C. Ratcliff were in consultation with the governor last week, and a plan of
    procedure was agreed upon." (Review 1912-09-12 p.1.) — Burns was on the case from 1912; the
    famous J.N. Wilkerson Burns-agency assignment (Mansfield/Jones theory) came 1916 [SECONDARY:
    Wikipedia, Smithsonian, Iowa Legislature PDF].
32. [CONTEMPORARY] Grand juries: October 1912 Montgomery County grand jury (foreman Walter
    Sellergren) "returned four indictments" — Spargur assault on Kelso and others; NO indictment
    in the Moore murders. December 1912 grand jury reported liquor indictments (John Patterson).
    (Review 1912-10-24 p.1; 1912-12-19 p.1.) The September 1912 term thus produced no murder
    indictment; the big murder grand juries came later (April 30, 1917 indictment of Kelly —
    CONTEMPORARY, Review 1917-05-19 p.2 / 1917-11-28 p.1; July 1916 grand jury declined to indict
    Mansfield — SECONDARY, Wikipedia).

### Rev. George Kelly (all CONTEMPORARY unless noted)
33. Indictment/surrender: Kelly "appeared in the county seat on a Monday morning in May [1917] and
    gave himself up following the indictment returned against him by a Montgomery county grand
    jury on the night of April 30th"; while awaiting trial he was held in the Logan (Harrison Co.)
    jail — "REV. KELLY IN LOGAN JAIL"; defense attorney T.J. Hysham: Kelly "traveled here to give
    himself up to answer the charge in spite of the attorney general's office... He said that
    Kelly was not arrested until after the county attorney had telephoned the attorney general."
    (Review 1917-11-28 p.1; 1917-05-19 p.2.) — The prompt's "arrest June 1913" is not supported;
    the 1914 event was an unrelated obscene-mail conviction [SECONDARY: Wikipedia].
34. First trial (Red Oak, Sept 1917): state's arguments Sept 25 (Attorney General Havner; defense
    Judge A.L. Sutton and T.J. Hysham); "the jury was 'hung'... T. C. Brown... caused the one-man
    deadlock in the jury room last week and held out till the finish against the acquittal";
    reported Oct 3, 1917; Kelly "will probably be placed on trial again within a few weeks."
    (Review 1917-10-03 p.1.) [SECONDARY: Iowa Cold Cases — "The jury deadlocked eleven to one for
    acquittal"; case to jury Sept 26.]
35. Second trial (Red Oak, Nov 1917): "The jury that heard Kelly's second trial for the Villisca ax
    murders of 1912 returned a verdict of 'not guilty' Saturday night at half past eight o'clock
    after considering the case four and one-half hours, the jury having retired at four o'clock.
    The freedom of the minister was decided on the first ballot." (Review 1917-11-28 p.1; semi-
    weekly edition, Wednesday Nov 28, 1917; Saturday = Nov 24.) — acquittal was NOVEMBER 1917,
    not June 1917.
36. Confession [SECONDARY quoting the confession]: Kelly signed a confession Aug 31, 1917 ("I
    killed the children upstairs first and the children downstairs last... 'Slay utterly' came to
    my mind...") — recanted at trial (Smithsonian; Iowa Cold Cases: signed "at 7 a.m." Aug 31,
    saying God whispered "suffer the children to come unto me").
37. Lena Stillinger controversy at trial: prosecutor — "Lena Stillinger, the oldest female child in
    the house... was pulled twenty inches down from the head of the bed. There was a smear of blood
    on one of her legs. The body was lying on the edge of the bed and the position of the limbs
    plainly indicated the work of a pervert"; defense reply — the "confession" was coerced,
    deputies "destroyed poor Kelly's reason until he babbled like a goose." (Review 1917-09-29
    p.2–3.) [SECONDARY: "Later investigations showed no evidence" of sexual assault (Wikipedia);
    "doctors concluded she had not been sexually abused" (Iowa Cold Cases).]

## Contradictions log
See timeline_notes contradictions embedded above; summary:
- Discovery time: 7:00 a.m. (Wikipedia/legis PDF) vs 7:30 a.m. Peckham alarm (Iowa Cold Cases) vs
  "about half past eight o'clock" house entered (Review, contemporaneous, p.1) vs Peckham's own
  testimony (arose 4–5 a.m., alarmed "toward eight o'clock").
- Time-of-death: midnight–2 a.m. (Wikipedia) vs midnight–5 a.m. (legis PDF) vs contemporaneous
  1–2 a.m. noise heard by Mrs. F.F. Jones (Review) vs "some time before 5 a.m." exit (Smithsonian).
- Entry: unlocked back door (Smithsonian/Iowa Cold Cases) vs all doors/windows locked, front-door
  key taken by killer (Review, contemporaneous).
- Lena's age: 11 (Review obituary; Wikipedia) vs 12 (Iowa Cold Cases; legis PDF "Lenae, 12";
  Smithsonian "12 and 9" — which also ages Ina as 9).
- Weapon provenance: "axe belonging to Josiah" (Wikipedia/legis PDF) vs "Joe's axe from the back
  yard" (Iowa Cold Cases) vs "probably taken from... the coal shed" (Smithsonian); Review says only
  "the ax found leaning against the wall close to the lamp."
- Bacon: 4-lb slab (Wikipedia/Iowa Cold Cases) vs 2-lb wrapped in a towel (Smithsonian).
- Bodies removed: "Monday night after midnight" (Review) vs "close to 2 a.m." after 10 p.m.
  permission (Wikipedia).
- Inquest opening: Review has sworn testimony beginning Tuesday June 11, 1:30 p.m., 11 witnesses
  by 3:30; Wikipedia says inquest "convened June 11" and describes coroner's jury viewing the
  house only "late afternoon" June 10 after arriving "later that morning."
- Burns agency: engaged by Iowa Attorney General by Sept 1912 (Review) vs "Burns agency (1916)
  under J.N. Wilkerson" framing (secondary literature).
- Kelly chronology: prompt's "arrest June 1913; first trial Sept 1917; acquittal June 1917" —
  contemporaneous record: indicted Apr 30 1917, jail May–Nov 1917, first trial hung (reported
  Oct 3, 1917), second trial verdict "not guilty" Nov 24, 1917.
- Lena resistance/sexual assault: state argued pervert's positioning at trial; secondary medical
  conclusion says no evidence of assault; degree of Lena's resistance varies by teller.
- Stillinger girls' arrival/overnight: invited by Katherine (Wikipedia) vs "asked their parents'
  permission to stay overnight" as neighbors (Iowa Cold Cases); review's "Two Daughters of Mr. and
  Mrs. J. T. Stillinger... the Victims" (Review headline).
- Prompt checks: victims' names/ages verified (Review obituaries match, except Lena 11 vs 12);
  "weapon = axe belonging to Josiah" only as SECONDARY; Children's Day program confirmed
  CONTEMPORARY + SECONDARY; coroner = A. L. Linquist (not "Dr. J.C. Linnas"); marshal = J. H.
  "Hank" Horton (Horton's nickname "Hank" appears only in SECONDARY sources in this set).

## SNIPPET-ONLY items
- newspapers.com/topics page (search snippet): lists contemporaneous headlines incl. "Eight People
  Are Murdered in Their Beds at Villisca, Sunday Night" (Evening Nonpareil, Council Bluffs, June
  10, 1912) and "Witnesses Tell of Discovering Eight Murdered Persons" (inquest testimony, June 11)
  — SNIPPET-ONLY, pages behind Newspapers.com paywall.
- KCRA 2023 piece, Trove 20 Jul 1912 "MANIACAL MURDER" (trove.nla.gov.au/newspaper/article/125982772)
  — located, not fetched this session.

## Inaccessible sources
- Chronicling America search API https://chroniclingamerica.loc.gov/search/pages/results/... — HTTP 404 (endpoint retired).
- Chronicling America page/OCR URLs https://chroniclingamerica.loc.gov/lccn/.../ocr.txt — HTTP 403 Cloudflare to non-browser clients.
- www.loc.gov collections API & resource viewer — Cloudflare interstitial not cleared in automation browser.
- The Day Book (Chicago) June 14, 1912, seq-1 OCR retrieved via Wayback Machine (front page has no Villisca content; the murder story sits on other pages whose OCR captures are not archived).
- Newspapers.com clippings/topics pages — paywall.
- NY Times 1917 (timesmachine.nytimes.com/timesmachine/1917/09/02/96264124.pdf) — paywalled; cited by Iowa Cold Cases.
