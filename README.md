# AUBRUSHLI

## WHAT IS IT?

[![Watch the video](https://img.youtube.com/vi/iqfSt_0BC3E/maxresdefault.jpg)](https://www.youtube.com/watch?v=iqfSt_0BC3E)

AUBRUSHLI allows specially formatted [fountain](https://fountain.io/) screenplays/scripts to automatically create CSVs for Cast lists, Breakdown Summaries and Shot lists thereby reducing duplication of work and potentially speeding up the production process. 

The name AUBRUSHLI is just an acronynm taking the first two letters of Automated Breakdown Shot List and adding a U in the middle. 

The application is a desktop app currently for MAC and Windows. 

## A QUICK DISCLAIMER

I made AUBRUSHLI for me initially after seeing some of the tools of the production process that were catered to only by professional fairly expensive software and then seeing the open source fountain script markup language and thinking ok maybe I can do something with this. So AUBRUSHLI at least right now is not at all robust and wants tags in a certain well defined format. I mean it shouldn't damage your script/screenplay but take a copy just in case. It obviously does not have a fraction of the functionality of the paid for solutions, nor is it remotely pretty, but it works and I may improve it over time and of course as its on github, others are free to if they wish. 

## INSTALLATION

Installation is just a case of downloading the zip file from the release for your particular os and unzipping and running https://github.com/StephanosPSteer/AUBRUSHLI/releases

## HOW IT WORKS

The AUBRUSHLI app makes use of [boneyard](https://fountain.io/syntax#section-bone) within fountain applications. When AUBRUSHLI sees a [boneyard tag](https://fountain.io/syntax#section-bone) i.e. /* some text */ instead of just ignoring it like fountain normally would AUBRUSHLI looks for specific tags within the boneyard in order to create Breakdown Summaries or Shot Lists.  

## BREAKDOWN SUMMARIES

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

* **Scene Number** - the scene number
* **Scene Name** - the scene name
* **TAG** - the breakdown summary tag 
* **Tagged Resource Required** - What do you actually need to get for the production
* **Surrounding Text** - Context for the resource you need
* **Start Line Index** - What line does it start on
* **Start Char Index** - Starting character
* **End Char Index** - Ending character

## SHOT LISTS

[![Watch the video](https://img.youtube.com/vi/Suh_3SY9-ZY/maxresdefault.jpg)](https://www.youtube.com/watch?v=Suh_3SY9-ZY)

Within fountain boneyard tags AUBRUSHLI when told to create a Shot List will look for an Opening TAG:-

* SHOTSTART #:

and a corresponding Closing Tag:-

* SHOTEND #:

If AUBRUSHLI finds an opening tag it will then look for the rest of the text until it finds a closing tag and will add the tag and all its surrounding text into a row in your CSV file, initially it also adds the following column headers into the top row in your CSV file:-
    
* **Shot Number** - The shot number
* **Scene Number** - The scene number
* **Scene Name** - The scene name
* **Shot Size** - e.g. wide, medium, close up
* **Shot Type** - e.g. single, double 
* **AngleOrigin** - the shot angle
* **MoveMent** - is it a static or moving shot
* **lens** - what lens or lens range
* **Sound** - does this sync with sound
* **Description** - description of the shot
* **Start Line Index** - the starting line index of SHOTSTART
* **Start Char Index** - the starting character index in SHOTSTART
* **End Char Index** - the ending character index of SHOTSTART
* **End Line Index** - the line index of SHOTEND
* **Surrounding Text** - all the text between the beginning of the SHOTSTART boneyard and end of SHOTEND boneyard

## CAST LISTS

Aubrushli also creates cast lists from any fountain document along with the frequency of dialogue of each character.

and thats the functionality of Aubrushli hope it helps you

Let me knowe if you have any comments or issues with Aubrushli


Many thanks to:-

https://fountain.io/

https://gist.github.com/ColtonProvias/8232624

https://github.com/chriskiehl/Gooey

https://github.com/pyinstaller/pyinstaller
