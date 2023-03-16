BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "shots" (
	"Shot_Number"	TEXT,
	"Scene_Number"	TEXT,
	"Scene_Name"	TEXT,
	"Shot_Size"	TEXT,
	"Shot_Type"	TEXT,
	"AngleOrigin"	TEXT,
	"MoveMent"	TEXT,
	"lens"	TEXT,
	"Sound"	TEXT,
	"Description"	TEXT,
	"Start_Line_Index"	TEXT,
	"Start_Char_Index"	TEXT,
	"End_Char_Index"	TEXT,
	"End_Line_Index"	TEXT,
	"Surrounding_Text"	TEXT
);
CREATE TABLE IF NOT EXISTS "ShotImages" (
	"Imageid"	INTEGER NOT NULL UNIQUE,
	"imagepath"	TEXT NOT NULL UNIQUE,
	"ShotID"	INTEGER NOT NULL,
	"seed"	INTEGER,
	PRIMARY KEY("Imageid" AUTOINCREMENT)
);
COMMIT;
