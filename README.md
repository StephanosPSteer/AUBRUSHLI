# AUBRUSHLI

WHAT IS IT?

[![Watch the video](https://img.youtube.com/vi/iqfSt_0BC3E/maxresdefault.jpg)](https://www.youtube.com/watch?v=iqfSt_0BC3E)

AUBRUSHLI allows specially formatted [fountain](https://fountain.io/) screenplays/scripts to automatically create CSVs for Cast lists, Breakdown Summaries and Shot lists thereby reducing duplication of work and potentially speeding up the production process. 

The name AUBRUSHLI is just an acronynm taking the first two letters of Automated Breakdown Shot List and adding a U in the middle. 

The application is a desktop app currently for MAC and Windows. 

A QUICK DISCLAIMER

I made AUBRUSHLI for me initially after seeing some of the tools of the production process that were catered to only by professional fairly expensive software and then seeing the open source fountain script markup language and thinking ok maybe I can do something with this. So AUBRUSHLI at least right now is not at all robust and wants tags in a certain well defined format. I mean it shouldn't damage your script/screenplay but take a copy just in case. It obviously does not have a fraction of the functionality of the paid for solutions, nor is it remotely pretty, but it works and I may improve it over time and of course as its on github, others are free to if they wish. 

INSTALLATION

Installation is just a case of downloading the zip file from the release for your particular os and unzipping and running https://github.com/StephanosPSteer/AUBRUSHLI/releases

HOW IT WORKS

The AUBRUSHLI app makes use of [boneyard](https://fountain.io/syntax#section-bone) within fountain applications. When AUBRUSHLI sees a [boneyard tag](https://fountain.io/syntax#section-bone) i.e. /* some text */ instead of just ignoring it like fountain normally would AUBRUSHLI looks for specific tags within the boneyard in order to create Breakdown Summaries or Shot Lists.  

BREAKDOWN SUMMARIES

[![Watch the video](https://img.youtube.com/vi/jxFoaLxFhfI/maxresdefault.jpg)](https://www.youtube.com/watch?v=jxFoaLxFhfI)



Within fountain boneyard tags AUBRUSHLI when told to create a breakdown summary will look for one of the following tags:-

* CAST:
* EXTRAS SILENT: 
* EXTRAS ATMOSPHERE: 
* PROPS: 
* WARDROBE:
* SPECIAL EQUIPMENT:
* COSTUMES:
* MAKEUP & HAIR:
* VEHICLES:
* STUNTS: 
* SOUND FX & MUSIC:
* PRODUCTION NOTES:
* GREENS:
* SPFX:
* LIVESTOCK:
* WRANGLER:
* VFX: 
* SET DRESSING:
* WEAPONS:

The tags I believe are fairly standard within Film and TV production. 

If AUBRUSHLI finds a tag it will then look for the rest of the text within the boneyard element and will add the tag and all the text in the boneyard and its surrounding text into a row in your CSV file, initially it also adds the following column headers into the top row in your CSV file:-

'Scene Number',  'Scene Name','TAG','Tagged Resource Required','Surrounding Text', 'Start Line Index', 'Start Char Index', 'End Char Index'

To demonstrate what I mean is simplest by an example. 

To be continued...

SHOT LISTS

[![Watch the video](https://img.youtube.com/vi/Suh_3SY9-ZY/maxresdefault.jpg)](https://www.youtube.com/watch?v=Suh_3SY9-ZY)

Within fountain boneyard tags AUBRUSHLI when told to create a Shot List will look for an Opening TAG:-

* SHOTSTART #:

and a corresponding Closing Tag:-

* SHOTEND #:

If AUBRUSHLI finds an opening tag it will then look for the rest of the text until it finds a closing tag and will add the tag and all its surrounding text into a row in your CSV file, initially it also adds the following column headers into the top row in your CSV file:-
    
'Shot Number', 'Scene Number', 'Scene Name',  'Shot Size','Shot Type','AngleOrigin','MoveMent', 'lens', 'Sound', 'Description', 'Start Line Index', 'Start Char Index', 'End Char Index', 'End Line Index', 'Surrounding Text'

CAST LISTS

Aubrushli also creates cast lists from any fountain document along with the frequency of dialogue of each character.

and thats the functionality of Aubrushli


Many thanks to:-

fountain.py https://gist.github.com/ColtonProvias/8232624

https://github.com/chriskiehl/Gooey

https://github.com/pyinstaller/pyinstaller
