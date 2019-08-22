#!/usr/bin/python
# egyptian opentype generator data

qcontrols = ['vj','hj','ts','bs','te','be','om','ss','se','cb','ce','cre','cfb','cfe','hwtb','hwte','hwttb','hwtte','hwtbb','hwtbe','hwtfb','hwtfe']

featurename = {
	'abvs' : {'prefix':'ab','name':'Above-base Substitutions','type':'GSUB'},
	'blws' : {'prefix':'bl','name':'Below-base Substitutions','type':'GSUB'},	
	'clig' : {'prefix':'cc','name':'Contextual Ligatures','type':'GSUB'},
	'mark' : {'prefix':'ma','name':'Mark Positioning','type':'GPOS'},
	'mkmk' : {'prefix':'mk','name':'Mark to Mark Positioning','type':'GPOS'},
	'pres' : {'prefix':'pr','name':'Pre-base Substitutions','type':'GSUB'},
	'psts' : {'prefix':'ps','name':'Post-base Substitutions','type':'GSUB'},
	'rlig' : {'prefix':'rl','name':'Required Ligatures','type':'GSUB'},
	'rtlm' : {'prefix':'rt','name':'Right-to-left alternates','type':'GSUB'},
	'vrt2' : {'prefix':'vr','name':'Vertical Alternates and Rotation','type':'GSUB'}
}

groupdata = {
	'bases_all' : ['quadratBases','quadratCartouches','quadratFortifieds','quadratCartouchesV','quadratFortifiedsV'],
	'cartoucheendsL' : ['csL','creL','ceL','hwtsL','hwteL','hwttsL','hwtteL','hwtbsL','hwtbeL','cfsL', 'cfeL','hfsL','hfeL'],
	'cartoucheendsR' : ['csR','creR','ceR','hwtsR','hwteR','hwttsR','hwtteR','hwtbsR','hwtbeR','cfsR', 'cfeR','hfsR','hfeR'],
	'cartoucheendsV' : ['csT','creB','ceB','hwtsT','hwteB','hwttsT','hwtteB','hwtbsT','hwtbeB','cfsT', 'cfeB','hfsT','hfeB'],
	'characters_all' : ['GB1'],
	'cobras' : ['F20','I1','I10','I11','I31','M10','V22','V23','V23a'],
	'colCounter' : ['hj2B','hj1B','hj0B','h0'],
	'colspacers0' : ['c0s4p0','c0s3p0','c0s2p0','c0s1p5','c0s1p0','c0s0p5','c0s0p66','c0s0p33','c0s0p25'],
	'colspacers0R' : ['c0s4p0R','c0s3p0R','c0s2p0R','c0s1p5R','c0s1p0R','c0s0p5R','c0s0p66R','c0s0p33R','c0s0p25R'],
	'colspacers1' : ['c1s3p0','c1s2p0','c1s1p0','c1s0p5','c1s0p33'],
	'colspacers1R' : ['c1s3p0R','c1s2p0R','c1s1p0R','c1s0p5R','c1s0p33R'],
	'colspacers2' : ['c2s1p0'],
	'colspacers2R' : ['c2s1p0R'],
	'controls_a' : ['controls_joiners','ss','se'],
	'controls_b' : ['hj1A','vj1A','hj0A','vj0A','hj2A','vj2A','corners0a','corners1a','om0A','om1A'],
    'controls_ng': ['Qi','Qf','m0','cleanup','ins1l0','ins1','et00','dda','mn4','mn3','mn2','ub'], #controls not grouped for injection
	'controls_joiners' : ['hj','vj','corners','om'],
	'corners' : ['ts','te','bs','be'],
	'corners0a' : ['its0A','ibs0A','cbr0A','ite0A','ibe0A','om0A'],
	'corners0b' : ['its0B','ibs0B','cbr0B','ite0B','ibe0B','om0B'],
	'corners0bNotOM' : ['its0B','ibs0B','cbr0B','ite0B','ibe0B'],
	'corners1a' : ['its1A','ibs1A','cbr1A','ite1A','ibe1A','om1A'],
	'corners1b' : ['its1B','ibs1B','cbr1B','ite1B','ibe1B','om1B'],
	'corners1bNotOM' : ['its1B','ibs1B','cbr1B','ite1B','ibe1B'],
	'counters_h' : ['ch0','ch1','ch2','ch3','ch4','ch5','ch6','ch7','ch8','ch9','ch10','ch11','ch12','ch13','ch14','ch15','ch16','ch17','ch18','ch19','ch20','ch21','ch22','ch23','ch24','ch25','ch26','ch27','ch28','ch29','ch30','ch31','ch32','ch33','ch34','ch35','ch36','chb'],
	'counters_v' : ['cv0','cv1','cv2','cv3','cv4','cv5','cv6','cv7','cv8','cv9','cv10','cv11','cv12','cv13','cv14','cv15','cv16','cv17','cv18','cv19','cv20','cv21','cv22','cv23','cv24','cv25','cv26','cv27','cv28','cv29','cv30','cv31','cv32','cv33','cv34','cv35','cv36','cvb'],
	'deltas' : ['dv1','dv2','dv3','dv4','dv5','dv6','dv7','dv8','dv9','dv10','dv11','dv12','dv13','dv14','dv15','dv16','dv17','dv18','dv19','dv20','dv21','dv22','dv23','dv24','dv25','dv26','dv27','dv28','dv29','dv30'],
	'deltas_sp' : ['ds5','ds4','ds3','ds2','ds1'],
	'deltas_cells' : ['dCells','en_all'],
	'deltas_spacers' : ['spacers_deltarows','cs0','rs0'],
	'deltas_all' : ['dd1','dv0','deltas','th6','th5','th4','th3','th2'],
	'dCells' : ['dc0','dc1','dc2','dc3','dc4','dc5'],
	'eh_all' : ['eh1','eh2','eh3','eh4','eh5','eh6','eh7','eh8'],
	'en_all' : ['en1','en2','en3','en4','en5','en6','enb'],
	'et_all' : ['et11','et12','et13','et14','et15','et16','et21','et22','et23','et24','et25','et26','et31','et32','et33','et34','et35','et36','et41','et42','et43','et44','et45','et46','et51','et52','et53','et54','et55','et56','et61','et62','et63','et64','et65','et66','et71','et72','et73','et74','et75','et76','et81','et82','et83','et84','et85','et86'],
	'ev_all' : ['ev1','ev2','ev3','ev4','ev5','ev6'],
	'expansionheights' : ['xv1','xv2','xv3','xv4','xv5'],
	'expansion_all' : ['rowplus','expansionheights'],
	'glyphs_all' : ['placeholder'],
	'groupCounters' : ['grp0','grp1','grp2'],
	'horizontals2' : ['eh_all','h1','h2','h3','h4','h5','h6','h7','h8'],
	'insertionmarkers': ['ima','imb','im0'],
	'insertionsizes1a' : ['it11a','it21a','it22a','it33a','it43a','it44a','it55a','it66a'],
	'insertionsizes1'  : ['it11' ,'it21' ,'it22' ,'it33' ,'it43' ,'it44' ,'it55' ,'it66'],
	'insertionsizes1R' : ['it11R','it21R','it22R','it33R','it43R','it44R','it55R','it66R'],
	'insertions' : ['insertionmarkers','insertionsizes1a'],
	'minsizes' : ['mt22','mt33','mt44','mt43','su'],
	'mirror_all' : [],
	'normalize' : ['dn1','dn2','dn3','dn4','dn5','hn1','hn2','hn3','hn4','hn5'],
	'parens' : ['parens_h','parens_v','corners0a','corners1a','om0A'],
	'parens_h' : ['c0bA','c0eA','c1bA','c1eA','c2bA','c2eA'],
	'parens_v' : ['r0bA','r0eA','r1bA','r1eA','r2bA','r2eA'],
	'quadratBases'      : ['QB1','QB2','QB3','QB4','QB5','QB6','QB7','QB8'],
	'quadratCartouches' : ['QC1','QC2','QC3','QC4','QC5','QC6','QC7','QC8'],
	'quadratCartouchesV' : ['QC1V','QC2V','QC3V','QC4V','QC5V','QC6V','QC7V','QC8V'],
	'quadratFortifieds' : ['QF1','QF2','QF3','QF4','QF5','QF6','QF7','QF8'],
	'quadratFortifiedsV' : ['QF1V','QF2V','QF3V','QF4V','QF5V','QF6V','QF7V','QF8V'],
	'rowCounter' : ['vj0B','vj1B','vj2B','v0'],
	'rowmaxes' : ['rm1','rm2','rm3','rm4','rm5','rm6','rc0','minsizes'],
	'rowplus' : ['rp1','rp2','rp3','rp4','rp5'],
	'rowspacers0' : ['r0s4p0','r0s3p0','r0s2p0','r0s1p5','r0s1p0','r0s0p5','r0s0p66','r0s0p33','r0s0p25'],
	'rowspacers0R' : ['r0s4p0R','r0s3p0R','r0s2p0R','r0s1p5R','r0s1p0R','r0s0p5R','r0s0p66R','r0s0p33R','r0s0p25R'],
	'rowspacers1' : ['r1s3p0','r1s2p0','r1s1p0','r1s0p5','r1s0p33'],
	'rowspacers1R' : ['r1s3p0R','r1s2p0R','r1s1p0R','r1s0p5R','r1s0p33R'],
	'rowspacers2' : ['r2s1p0'],
	'rowspacers2R' : ['r2s1p0R'],
	'shapeheights' : ['sv1','sv2','sv3','sv4','sv5','sv6'],
	'shapes_0' : ['o86','o85','o84','o83','o82','o81','o76','o75','o74','o73','o72','o71','o66','o65','o64','o63','o62','o61','o56','o55','o54','o53','o52','o51','o46','o45','o44','o43','o42','o41','o36','o35','o34','o33','o32','o31','o26','o25','o24','o23','o22','o21','o16','o15','o14','o13','o12','o11'],
	'shapes_1' : ['s66','s65','s64','s63','s62','s61','s56','s55','s54','s53','s52','s51','s46','s45','s44','s43','s42','s41','s36','s35','s34','s33','s32','s31','s26','s25','s24','s23','s22','s21','s16','s15','s14','s13','s12','s11'],
	'shapes_2' : ['i66','i65','i64','i63','i62','i61','i56','i55','i54','i53','i52','i51','i46','i45','i44','i43','i42','i41','i36','i35','i34','i33','i32','i31','i26','i25','i24','i23','i22','i21','i16','i15','i14','i13','i12','i11'],
	'shapeinsertions0' : ['shapes_0','ih0','iv0','shapes_ts','shapes_bs','shapes_te','shapes_be','shapes_cb','shapes_om'],
	'insertionsizes' : ['ih1','ih2','ih3','ih4','ih5','ih6','iv2','iv3','iv4','iv5','iv6'],
	'shapes_insert0_POS' : ['o66','o65','o64','o63','o62','o56','o55','o54','o53','o52','o46','o45','o44','o43','o42','o36','o35','o34','o33','o32','o26','o25','o24','o23','o22'],
	'shapes_ts' : ['ts66','ts65','ts64','ts63','ts62','ts56','ts55','ts54','ts53','ts52','ts46','ts45','ts44','ts43','ts42','ts36','ts35','ts34','ts33','ts32','ts26','ts25','ts24','ts23','ts22'],
	'shapes_bs' : ['bs66','bs65','bs64','bs63','bs62','bs56','bs55','bs54','bs53','bs52','bs46','bs45','bs44','bs43','bs42','bs36','bs35','bs34','bs33','bs32','bs26','bs25','bs24','bs23','bs22'],
	'shapes_te' : ['te66','te65','te64','te63','te62','te56','te55','te54','te53','te52','te46','te45','te44','te43','te42','te36','te35','te34','te33','te32','te26','te25','te24','te23','te22'],
	'shapes_be' : ['be66','be65','be64','be63','be62','be56','be55','be54','be53','be52','be46','be45','be44','be43','be42','be36','be35','be34','be33','be32','be26','be25','be24','be23','be22'],
	'shapes_cb' : ['cb66','cb65','cb64','cb63','cb62','cb56','cb55','cb54','cb53','cb52','cb46','cb45','cb44','cb43','cb42','cb36','cb35','cb34','cb33','cb32','cb26','cb25','cb24','cb23','cb22'],
	'shapes_om' : ['om66','om65','om64','om63','om62','om61','om56','om55','om54','om53','om52','om51','om46','om45','om44','om43','om42','om41','om36','om35','om34','om33','om32','om31','om26','om25','om24','om23','om22','om21','om16','om15','om14','om13','om12','om11'],
	'shapes_u'  : ['es66','es65','es64','es63','es62','es61','es56','es55','es54','es53','es52','es51','es46','es45','es44','es43','es42','es41','es36','es35','es34','es33','es32','es31','es26','es25','es24','es23','es22','es21','es16','es15','es14','es13','es12','es11'],
	'shapes_ls' : ['ls66','ls65','ls64','ls63','ls62','ls61','ls56','ls55','ls54','ls53','ls52','ls51','ls46','ls45','ls44','ls43','ls42','ls41','ls36','ls35','ls34','ls33','ls32','ls31','ls26','ls25','ls24','ls23','ls22','ls21','ls16','ls15','ls14','ls13','ls12','ls11'],
	'shapewidths' : ['sh1','sh2','sh3','sh4','sh5','sh6','sh7','sh8'],
	'spacers_cols0'  : ['cs0','c0s1p0','c0s0p5','c0s0p66','c0s0p33','c0s0p25'], # ORDER OF THESE ITEMS IS IMPORTANT
	'spacers_cols1'  : ['cs0','c1s1p0','c1s0p5','cs0','c1s0p33','cs0'], # ORDER OF THESE ITEMS IS IMPORTANT
	'spacers_cols2'  : ['cs0','c2s1p0','cs0','cs0','cs0','cs0'], # ORDER OF THESE ITEMS IS IMPORTANT
	'spacers_deltas' : ['ds0','ds1p0','ds0p5','ds0p66','ds0p33','ds0p25'], # ORDER OF THESE ITEMS IS IMPORTANT
	'spacers_rows0'    : ['rs0','r0s4p0','r0s3p0','r0s2p0','r0s1p5','r0s1p0','r0s0p5','r0s0p66','r0s0p33','r0s0p25'], # ORDER OF THESE ITEMS IS IMPORTANT
	'spacers_rows1'    : ['rs0','rs0','r1s3p0','r1s2p0','rs0','r1s1p0','r1s0p5','rs0','r1s0p33','rs0'], # ORDER OF THESE ITEMS IS IMPORTANT
	'spacers_rows2'    : ['rs0','rs0','rs0','rs0','rs0','r2s1p0','rs0','rs0','rs0','rs0'], # ORDER OF THESE ITEMS IS IMPORTANT
	'spacers_deltarows': ['ds0','ds4p0','ds3p0','ds2p0','ds1p5','ds1p0','ds0p5','ds0p66','ds0p33','ds0p25'], # ORDER OF THESE ITEMS IS IMPORTANT
	'stems0-h'  : ['c0h1', 'c0h2', 'c0h3', 'c0h4', 'c0h5', 'c0h6', 'c0h7', 'c0h8', 'colspacers0', 'r0eB'],
	'stems0-hR' : ['c0h1R','c0h2R','c0h3R','c0h4R','c0h5R','c0h6R','c0h7R','c0h8R','colspacers0R','r0eBR'],
	'stems0-v'  : ['r0v1', 'r0v2', 'r0v3', 'r0v4', 'r0v5', 'r0v6', 'rowspacers0'],
	'stems0-vR' : ['r0v1R','r0v2R','r0v3R','r0v4R','r0v5R','r0v6R','rowspacers0R'],
	'stems1-h'  : ['c1h1', 'c1h2', 'c1h3', 'c1h4', 'c1h5', 'c1h6', 'colspacers1','r1eB'],
	'stems1-hR' : ['c1h1R','c1h2R','c1h3R','c1h4R','c1h5R','c1h6R','colspacers1R','r1eBR'],
	'stems1-v'  : ['r1v1', 'r1v2', 'r1v3', 'r1v4', 'r1v5', 'r1v6', 'rowspacers1','insertionsizes1','r1sep'],
	'stems1-vR' : ['r1v1R','r1v2R','r1v3R','r1v4R','r1v5R','r1v6R','rowspacers1R','insertionsizes1R','r1sepR'],
	'stems2-h'  : ['c2h1', 'c2h2', 'c2h3', 'c2h4', 'colspacers2', 'r2eB'],
	'stems2-hR' : ['c2h1R','c2h2R','c2h3R','c2h4R','colspacers2R','r2eBR'],
	'stems2-v'  : ['r2v1', 'r2v2', 'r2v3', 'r2v4', 'r2v5', 'r2v6', 'r2vb','rowspacers2'],
	'stems2-vR' : ['r2v1R','r2v2R','r2v3R','r2v4R','r2v5R','r2v6R','r2vbR','rowspacers2R'],
	'stems_12' : ['stems1-h','stems1-v','stems2-h','stems2-v','ub'],
	'targets' : ['t86','t85','t84','t83','t82','t81','t76','t75','t74','t73','t72','t71','t66','t65','t64','t63','t62','t61','t56','t55','t54','t53','t52','t51','t46','t45','t44','t43','t42','t41','t36','t35','t34','t33','t32','t31','t26','t25','t24','t23','t22','t21','t16','t15','t14','t13','t12','t11'], #Not in use
	'targetwidth' : ['trg2', 'trg3', 'trg4', 'trg5', 'trg6'],
	'verticals2' : ['v1','v2','v3','v4','v5','v6','deltas_sp']
} 

basetypes = ['QB1','QB2','QB3','QB4','QB5','QB6','QB7','QB8',
    'QC1','QC2','QC3','QC4','QC5','QC6','QC7','QC8',
    'QF1','QF2','QF3','QF4','QF5','QF6','QF7','QF8',
    'QC1V','QC2V','QC3V','QC4V','QC5V','QC6V','QC7V','QC8V',
    'QF1V','QF2V','QF3V','QF4V','QF5V','QF6V','QF7V','QF8V',
	'csL','creL','ceL','hwtsL','hwteL','hwttsL','hwtteL','hwtbsL','hwtbeL','cfsL', 'cfeL','hfsL','hfeL',
	'csR','creR','ceR','hwtsR','hwteR','hwttsR','hwtteR','hwtbsR','hwtbeR','cfsR', 'cfeR','hfsR','hfeR',
	'csT','creB','ceB','hwtsT','hwteB','hwttsT','hwtteB','hwtbsT','hwtbeB','cfsT', 'cfeB','hfsT','hfeB',
	'Qf','Qi','vjV','hjV','tsV','bsV','teV','beV','omV','ssV','seV'
]

internalmirrors = {
	'D54':'D55','D55':'D54','F46':'F47','F46a':'F47a','F47':'F46','F47a':'F46a','F48':'F49',
	'F49':'F48','L6':'L6a','L6a':'L6','O5':'O5a','O5a':'O5','O50a':'O50b','O50b':'O50a',
	'U6a':'U6b','U6b':'U6a','V31':'V31a','V31a':'V31','Y3':'Y4','Y4':'Y3','J7':'J7a','J7a':'J7'
}

mirroring = {
	'A1','A2','A3','A4','A5','A5a','A6','A6a','A6b','A7','A8','A9','A10','A11',
	'A12','A13','A14','A14a','A15','A16','A17','A17a','A18','A19','A20','A21','A22',
	'A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A32a','A33','A34',
	'A35','A36','A37','A38','A39','A40','A40a','A41','A42','A42a','A43','A43a',
	'A44','A45','A45a','A46','A47','A48','A49','A50','A51','A52','A53','A54','A55',
	'A56','A57','A58','A59','A60','A61','A62','A63','A64','A65','A66','A67','A68',
	'A69','A70','B1','B2','B3','B4','B5','B5a','B6','B7','B8','B9','C1','C2','C2a',
	'C2b','C2C','C3','C4','C5','C6','C7','C8','C9','C10','C10a','C11','C12','C13',
	'C14','C15','C16','C17','C18','C19','C20','C21','C22','C23','C24','D1','D3',
	'D4','D5','D6','D7','D8','D8a','D9','D10','D11','D13','D14','D15','D16','D17',
	'D18','D19','D20','D26','D29','D30','D31','D33','D34','D34a','D36','D37','D38',
	'D39','D40','D41','D42','D43','D44','D45','D46','D46a','D47','D48','D48a','D49',
	'D50','D50a','D50b','D50c','D50d','D50e','D50f','D50g','D50h','D50i','D51',
	'D52','D52a','D53','D54a','D56','D57','D58','D59','D60','D61','D62','D63','D64',
	'D65','D66','E1','E2','E3','E4','E5','E6','E7','E8','E8a','E9','E9a','E10',
	'E11','E12','E13','E14','E15','E16','E16a','E17','E17a','E18','E19','E20',
	'E20a','E21','E22','E23','E24','E25','E26','E27','E28','E28a','E29','E30','E31',
	'E32','E33','E34','E34a','E36','E37','E38','F1','F1a','F2','F3','F4','F5','F6',
	'F7','F8','F9','F10','F11','F12','F14','F15','F16','F17','F18','F19','F20',
	'F21','F21a','F22','F23','F24','F25','F26','F27','F29','F30','F32','F33','F37',
	'F37a','F38','F38a','F39','F40','F42','F44','F50','F51','F51a','F51b','F51C',
	'F52','F53','G1','G2','G3','G4','G5','G6','G6a','G7','G7a','G7b','G8','G9',
	'G10','G11','G11a','G12','G13','G14','G15','G16','G17','G18','G19','G20','G20a',
	'G21','G22','G23','G24','G25','G26','G26a','G27','G28','G29','G30','G31','G32',
	'G33','G34','G35','G36','G36a','G37','G37a','G38','G39','G40','G41','G42','G43',
	'G43a','G44','G45','G45a','G46','G47','G48','G49','G50','G51','G52','G53','G54',
	'H1','H2','H3','H4','H5','H6','H6a','H7','H8','I1','I2','I3','I4','I5','I5a',
	'I6','I7','I8','I9','I9a','I10','I10a','I11','I11a','I12','I13','I14','I15',
	'K1','K2','K3','K4','K5','K6','K7','K8','L1','L2','L2a','L3','L4','L5','M1a',
	'M1b','M2','M3','M3a','M4','M5','M6','M7','M9','M10','M10a','M11','M12','M12a',
	'M12b','M12c','M12d','M12e','M12f','M12g','M12h','M14','M17','M17a','M18','M19',
	'M20','M21','M22','M22a','M23','M24','M25','M26','M27','M28','M29','M30','M33',
	'M33a','M33B','M36','M37','M38','M40','M40a','M41','M43','N2','N3','N6','N13',
	'N20','N21','N22','N23','N29','N32','N34','N34a','N37a','N39','N40','NL1','NL2',
	'NL3','NL4','NL5','NL5a','NL6','NL7','NL8','NL9','NL10','NL11','NL12','NL13',
	'NL14','NL15','NL16','NL17','NL17a','NL18','NL19','NL20','NU1','NU2','NU3',
	'NU4','NU5','NU6','NU7','NU8','NU9','NU10','NU10a','NU11','NU11a','NU12','NU13',
	'NU14','NU15','NU16','NU17','NU18','NU18a','NU19','NU20','NU21','NU22','NU22a',
	'O3','O4','O6','O7','O8','O9','O10','O10a','O10B','O10C','O11','O12','O13',
	'O14','O15','O16','O17','O18','O19','O19a','O20','O29','O30','O30a','O33a',
	'O35','O37','O38','O40','O42','O44','O45','O46','O47','O51','P1','P1a','P2',
	'P3','P3a','P5','P7','P9','P10','P11','Q1','Q2','Q7','R1','R2','R3','R5','R6',
	'R7','R8','R9','R10','R10a','R12','R13','R14','R15','R16','R17','R18','R19',
	'R25','R27','R29','S1','S2','S2a','S3','S4','S5','S6','S6a','S7','S8','S9',
	'S10','S13','S14a','S14b','S18','S19','S26','S28','S29','S30','S31','S32','S33',
	'S37','S38','S39','S40','S41','S44','S45','S46','T1','T2','T4','T5','T6','T7',
	'T7a','T11','T12','T13','T14','T15','T16','T16a','T17','T18','T19','T20','T21',
	'T24','T25','T26','T27','T29','T30','T31','T32','T32a','T33','T33a','T34','T35',
	'T36','U1','U2','U3','U4','U5','U6','U7','U8','U9','U10','U11','U12','U13',
	'U14','U15','U16','U17','U18','U19','U20','U21','U24','U25','U29a','U30','U31',
	'U32','U32a','U33','U35','U37','U38','U39','U40','V1','V1a','V1b','V1c','V1d',
	'V1e','V1f','V1g','V1h','V1i','V2','V2a','V3','V4','V10','V11','V11a','V11B',
	'V11C','V12','V12a','V12B','V13','V14','V15','V21','V22','V23','V23a','V25',
	'V28a','V29a','V33','V34','V35','V36','V37','V37a','V40','V40a','W9','W9a',
	'W10a','W14a','W15','W16','W17a','W20','W25','X5','X6a','X7','Y1a','Y7','Z4',
	'Z4a','Z5','Z5a','Z6','Z7','Z9','Z10','Z12','Z14','Z16d','Z16f','J1','J2','J3',
	'J4','J7b','J10','J11','J13','J14','J15','J16','J17','J18','J22','J26','J28',
	'J29','J31','J32'	
}