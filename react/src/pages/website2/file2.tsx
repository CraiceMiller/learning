import React from 'react';
import type {Component} from "@utils/typing" ; 
import { FaFire,FaAngleDown,FaAdjust} from "react-icons/fa" ; //NEW LIBRARY. 17/11/2025 
import {SlotItem, SwapyContainer} from "@lib/swap" ; 

/**
 new stuff i learned today Monday 17/11/2025
window.localStorage //this
window.document.body.classList
 
 */



/**
 * 
 * @returns 
 */








const SideBarIcon = ({icon, text='my icon :3'}:{icon:React.ReactNode,text?:string})=>
{
    return (
        <div className="sidebar-icon group  " >
            {icon}
            <span className='sidebar-tooltip group-hover:scale-100' >
                 {text}
            </span>

        </div>
    )
}

/**
 * @since 16/11/2025
 * @returns 
 */
function SideBar():Component
{
    return (
        <nav className='text-white bg-fourth h-screen w-56  
          p-1 flex flex-col shadow-lg justify-items-center
          dark-4
              '  >
            <h1>Side Bar</h1>
            <div>
                 <SideBarIcon  icon={<FaFire size={28}  /> } />
                 <SideBarIcon  icon={<FaAngleDown size={28}  /> } />
                 <SideBarIcon  icon={<FaAdjust size={28}  /> } />
            </div>
        </nav>
    )

}
// In your component file (e.g., ThemeIcon or another component)

function MyStyledComponent() {
    return (
      <div className="bg-white dark:bg-gray-900 min-h-screen">
        <h1 
          className="
            text-2xl 
            text-blue-700          {/* Default (Light) Text Color */}
            dark:text-gray-200    {/* Dark Mode Text Color */}
            bg-gray-100           {/* Default (Light) Background */}
            dark:bg-gray-800      {/* Dark Mode Background */}
            p-4 rounded
          "
        >
          Welcome!
        </h1>
        {/* ... your ThemeIcon component goes here to toggle the class ... */}
      </div>
    );
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

## customize properties
in our tailwindcss file we can create our customized properties to work in our
enviroment. 
using the `@layer` keyworkd along the word "component": 
`@layer components {}`
inside it we can work like a normal css file. using the class properties, using the dot (.) at
the beginning of the word. and inside our customzed class we can write our code. Note
we need to write the @apply keyword that this works property
.Box  {
        @apply relative flex items-center justify-center
          bg-gray-800 text-green-400
           hover:bg-green-600 
           hover:rounded-xl 
           transition-all duration-300 ease-linear
           square
           ; 
    }


## Groups 
in tailwindcss we can apply classes to a child element when
the father is hoover. 
A group is clever way to apply classes to a child when the state of the 
parent changes, However, groups do not work property in an @apply. 
To accomplish this task we only need to type <<group>> in our father element 
and then apply a rule in a child element, like a hover. 
```
    return (
        <div className="sidebar-icon group " >
            {icon}
            <span className='sidebar-tooltip group-hover:scale-100' >
                 {text}
            </span>

        </div>
    )
```

 */
function Content2():Component
{
    return (
        <section className='m-5 p-6 border-solid-2 w-full ' >
            <h1 className="bg-yellow-800  text-7x1  
            text-center hover:text-fuchsia-500 text-white
             " >Hello World </h1>
            <h1>Nice World i Have Here, arent I ? </h1>
            <MyStyledComponent />
        </section>
    )

}
function Content3():Component
{
    let Boxes:React.JSX.Element[] = [] ; 
    const CreateBox = (n:number|string)=>(
        <SlotItem itemName={`Item-No-${n}`} slotName={`Slot-No-${n}`} >
           <div className='square-2 dark-5 justify-center text-4xl
           align-middle bg-blue-300
           ' >{n}</div>
        </SlotItem>
    )

    for (let i :number = 1 ; i<=15 ; i++)
    {
        Boxes.push(CreateBox(i)) ; 

    }

    return (
        <SwapyContainer className=' bg-gray-50 dark-1 
        grid grid-cols-4 grid-rows-4 w-[120vw] mx-4
        ' >
            {Boxes}
        </SwapyContainer>
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


export default function App():Component
{
    
    return (
        <div className='flex flex-row justify-between ' >
            <SideBar/>
            <Content3 />
           { <Content2 />}
        

        </div>
    )
}