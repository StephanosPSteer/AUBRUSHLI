# AUBRUSHLI

WHAT IS IT?

AUBRUSHLI is an extension of fountain.py from... Which now allows specially formatted fountain screenplays/scripts to automatically create CSVs for Cast lists, Breakdown Summaries and Shot lists thereby reducing duplication of work and potentially speeding up the production process. 

The name AUBRUSHLI is just an acronynm taking the first two letters of Automated Breakdown Shot List and adding a U in the middle. 

The application is a desktop app currently for MAC and Windows. 

A QUICK DISCLAIMER

I made AUBRUSHLI for me initially after seeing some of the tools of the production process that were catered to only by professional fairly expensive software and then seeing the open source fountain script markup language and thinking ok maybe I can do something with this. So AUBRUSHLI at least right now is not at all robust and wants tags in a certain well defined format. I mean it shouldn't damage the script but take a copy. It obviously does not have a fraction of the functionality of the paid for solutions, nor is it remotely pretty, but it works and I may improve it over time and of ourse as its on github others are free to. 

INSTALLATION

Installation is just a case of downloading the zip file from the release for your particular os and unzipping and running https://github.com/StephanosPSteer/AUBRUSHLI/releases/tag/AUBRUSHLI

HOW IT WORKS

The AUBRUSHLI app makes use of boneyard within fountain applications. When AUBRUSHLI sees a boneyard tag i.e. /* some text */ instead of just ignoring it like fountain normally would AUBRUSHLI looks for specific tags in order to create Breakdown Summaries or Shot Lists.  

Breakdown Summaries
within boneyard tags AUBRUSHLI when told to create a breakdown summary will look for one of the following tags:-

CAST:
EXTRAS SILENT: 
EXTRAS ATMOSPHERE: 
PROPS: 
WARDROBE:
SPECIAL EQUIPMENT:
COSTUMES:
MAKEUP & HAIR:
VEHICLES:
STUNTS: 
SOUND FX & MUSIC:
PRODUCTION NOTES:
GREENS:
SPFX:
LIVESTOCK:
WRANGLER:
VFX: 
SET DRESSING:
WEAPONS:

The tags I believe are fairly standard within Film and TV production. 

If AUBRUSHLI finds a tag it will then look for the rest of the text within the boneyard element and will add the tag and all the text in the boneyard and its surrounding text into a row in a CSV file. In fact it adds the following columns into a row in a CSV file:-

'Scene Number',  'Scene Name','TAG','Tagged Resource Required','Surrounding Text', 'Start Line Index', 'Start Char Index', 'End Char Index'

To demonstrate what I mean is simplest by an example. 

To be continued...

SHOT LISTS

TAGS:-

SHOTSTART
SHOTEND
    
CSV ROW:-    
        
'Shot Number', 'Scene Number', 'Scene Name',  'Shot Size','Shot Type','AngleOrigin','MoveMent', 'lens', 'Sound', 'Description', 'Start Line Index', 'Start Char Index', 'End Char Index', 'End Line Index', 'Surrounding Text'

To be Continued...
