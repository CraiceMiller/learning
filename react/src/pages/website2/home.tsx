import * as React from 'react';
import { useState, useEffect } from 'react';
import type {Component} from "@utils/typing" ; 
import {SwapyContainer,CreateItem,CreateSlot } from "@lib/swap" ; 
import { Card} from "@components/cards" ; 

/**
 # How to install React-TypeScrict
 15/11/2025
1. first step is donwoload Node.js from the website and have a code editator like "vscode"
seconds step: 
2. open the terminal 
 type this: 

    `npm create vite@latest`

    it will ask you "Need to install the following packages: create-vite@8.1.0, Ok to proceed? (y) "
    press 'y' or/and  later this one will ask us the name we want to give it. 
    It will display you a list of frameworks to work with: 
           ○ Vanilla
        │  ○ Vue
        │  ● React
        │  ○ Preact
        │  ○ Lit
        │  ○ Svelte
        │  ○ Solid
        │  ○ Qwik
        │  ○ Angular
        │  ○ Marko
        │  ○ Others
    this time we want React , and press enter, then select type to work : 
            ○ TypeScript
        │  ● TypeScript + React Compiler
        │  ○ TypeScript + SWC
        │  ○ JavaScript
        │  ○ JavaScript + React Compiler
        │  ○ JavaScript + SWC
        │  ○ React Router v7 ↗
        │  ○ TanStack Router ↗
        │  ○ RedwoodSDK ↗
        │  ○ RSC ↗
    we want typeScript. 
3. Now it will as you 
    ◆  Install with npm and start now?
    │   ● Yes / ○ No
if you press yes it will automaticlly do all the thing for you: 
but if you press "No", do the following: 
    `cd *the folder name you provided it * `
    `npm install`
    `npm run dev`
and this is pretty much it .


# Extra Modules /Libraries to work with React: 
1. vite-tsconfig-paths
2. react-router-dom
3. react-toastify 
4. swapy
5. @tanstack/react-query



trick; we can install multiplies libraries at once
`npm install vite-tsconfig-paths react-router-dom  swapy ` 

 */



function MyCards()
{
    return (
        <div>
            <h2>Characters  </h2>

            <SwapyContainer style={{overflow:'auto', display:'flex',flexDirection:'row',justifyContent:'space-around',gap:'15px'}} >

                    <CreateSlot slotName='slot-1' >
                        <CreateItem itemName='Ayuko-Oka'>
                             <Card className='card' Title='Ayuko Oka' Imgsrc='https://i.pinimg.com/originals/36/db/3f/36db3f49e2c8278e09ef3600fc9c5fb2.jpg'>
                                <p> Oka is very short (only 143 cm tall / 4 feet 8 inches tall), and therefore has a body that resembles that of an innocent girl. However, she has rather large breasts and an hourglass figure like that of an adult model, which gives healthy guys like her boyfriend, Ueno, mixed feelings about her appearance.</p>
                             </Card>
                        </CreateItem>
                    </CreateSlot>

                    <CreateSlot slotName='slot-2' >
                        <CreateItem itemName='Makoto-Urabe' >
                            <Card className='card' Title='Makoto Urabe' Imgsrc='https://ghostlightning.wordpress.com/wp-content/uploads/2012/06/nazo-no-kanojo-mysterious-girlfriend-x-urabe-blushes.jpg'>
                            <p> By nature, Urabe is a girl of few words and very little facial expression. She appears to be very stoic, displaying very few visible emotions. This, however, is not the case. In reality, Urabe experiences the same range of emotions as anyone else, although she experiences some of them in slightly different ways.

                                When she gets excited or something makes her very happy, her mouth secretes a lot of saliva, causing her to vomit (she confesses this in episode 1 of the anime series).

                                She can be quite antisocial, not seeking out friends, and in some cases.</p>
                            </Card>
                        </CreateItem>
                        
                    </CreateSlot>

            </SwapyContainer>

        </div>

    )
}

function Content1()
{
    return (
    <div style={{marginBottom:'10vw', display:'flex',gap:'10vw',flexDirection:'column'}}>
        <div style={{padding:'5px',margin:'0 15vw',justifyContent:'center',textAlign:'center'}} >
            <h1>Nazo No Kanojo X / My Misterious Girfriend</h1>
            <p>Tsubaki Akira happens to lick the saliva of Urabe Mikoto, who just transferred into his class. This brings about a fever for Tsubaki. Urabe claims the cause is lovesickness which her saliva can cure. </p>
            <p> Audio: Japanese
            Subtitles: English, Español (América Latina), Português (Brasil)
            Content Advisory: Nudity, Suggestive Dialogue
            Genres: 
            </p>
            <MyCards />
        </div>

        <div  style={{alignItems:'center', margin:'20px 0', backgroundColor:'#E8DFD0' ,width:'100%',height:'200px', display:'flex',flexDirection:'row',justifyContent:'space-around',gap:'15px'}}>
            <div> 
                <img className=' hover:bg-gray-500' src='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/254345be-833a-4774-88db-bd872c70afc6/demk6n4-e480d0b0-5bf8-4236-a445-c5ca8b793616.png' />
            </div>
            <div>
                <h2 style={{borderBottom:'2px solid white'}} >Why I love this Animes so badly </h2>
                <p>This is the best anime ever </p>
            </div>
        </div>
    </div>

    )
}




/**
# Tailwindcss
16/11/2025, Sunday , thanks to Fireship (youtbe channel)
we set propeterties with the tag className, 
className='fixed text-center ' 
we can use square brackets to give very speficic information to it 
top-[-20px]
we can customize our color writting this: 
theme: {
    extend: {
      //color 16/11/2025
      colors:{
        first:"#EDE7DB", 
        second:"#E8DFD0 ", 
        third:"#663322 ", 
        fourth:"#422E30", 
        fifth:"#CC8356", 
        gray:colors.trueGray,

      }
    },
  },
we also can use the require function to set our color : 
const colors = require('tailwindcss/colors') ; 



 */
function Content2():Component
{
    return (
        <section className='m-5 p-6 border-solid-2 ' >
            <h1 className="bg-yellow-800  text-7x1  text-center hover:text-fuchsia-500 text-white " >Hello World </h1>
        </section>
    )

}

/**
 
{
  "name": "package.js",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "tsc && vite",
    "build": "tsc -b && vite build",
    "lint": "eslint .",
    "preview": "vite preview",
    "start": "dotenv -- node dist/index.js"
  },
  "dependencies": {
    "@tailwindcss/vite": "^4.1.17",
    "@tanstack/react-query": "^5.90.7",
    "react": "^19.1.1",
    "react-dom": "^19.1.1",
    "react-router-dom": "^7.9.4",
    "react-toastify": "^11.0.5",
    "swapy": "^1.0.5"
  },
  "devDependencies": {
    "@eslint/js": "^9.36.0",
    "@tailwindcss/cli": "^4.1.17",
    "@types/node": "^24.6.0",
    "@types/react": "^19.1.16",
    "@types/react-dom": "^19.1.9",
    "@vitejs/plugin-react": "^5.0.4",
    "autoprefixer": "^9.8.8",
    "babel-plugin-react-compiler": "^19.1.0-rc.3",
    "eslint": "^9.36.0",
    "eslint-plugin-react-hooks": "^5.2.0",
    "eslint-plugin-react-refresh": "^0.4.22",
    "globals": "^16.4.0",
    "postcss": "^7.0.39",
    "prettier-plugin-tailwindcss": "^0.7.1",
    "tailwindcss": "npm:@tailwindcss/postcss7-compat@^2.2.17",
    "typescript": "~5.9.3",
    "typescript-eslint": "^8.45.0",
    "vite": "npm:rolldown-vite@7.1.14",
    "vite-tsconfig-paths": "^5.1.4"
  },
  "overrides": {
    "vite": "npm:rolldown-vite@7.1.14"
  }
}

 */

/**Sky.2025*/
/** */
export default function App():Component
{
    const [user,setUser] = React.useState<string> ('') ; 

    return (
        <main className='' >
            <img 
            height={'400px'}
            width={'100%'}
            id='Nazo-no-Kanojo-Image'
            src='https://images7.alphacoders.com/843/843255.png'
            />
            <Content1 />
            <Content2/>
        </main>
    )
}

/**
 deletat the node libraries 

 Remove-Item -Path node_modules -Recurse -Force

 */