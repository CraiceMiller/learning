import {NavigationContainer } from "@layouts/navBar" ; 
import type {RouteData} from "@utils/typing" ; 
import { NavigationRoutes} from "@layouts/navBar"; 
import {SideBarContainer} from "@layouts/sideBar" ; 
import {NavigationBar } from "@layouts/navBar" ; 
import React from  "react" ; 
//styles
import "@styles/StyleWebsite2.css" ; 
//Website 
import {Header,Footer } from "@layouts/website2HF" ; 
import Home from "./website2/home" ; 
import Page2 from "./website2/file2" ; 
import Page3 from "./website2/myvidoes" ; 
import Page4 from "./website2/learn" ; 
import Grid from "./website2/mgrid" ; 
import Position from "./website2/positioning" ; 
import NewHooks from "./website2/newHooks"; 
import {FaFire, FaAdjust, FaAccessibleIcon } from "react-icons/fa" ; 



/**
 start: 14/11/2025 at 13:00 hrs , Friday 
 problesm route :( 24/11/2025 10:00 - 15:00)

 */

//Creating subChild
export const  SubChildsArray:RouteData[]=  [
    {
        //24 11 2025 
        element:Grid,
        text:<><FaFire  /> <p>My Grid</p> </>  , 
        to:"/learn/grid"
    },
    {
        element:Page2,
        text:<><FaAdjust  /> <p>  Whatever stuffs </p> </> , 
        to:"/learn/Page2"
    }, 
    {
        //28 / 11 / 2025, Friday at 16:00hrs
        element:Position,
        text:<><FaAccessibleIcon  /> <p>  Position Property </p> </> , 
        to:"/learn/position"
    }, 
    {
         //4-12-2025 Thursday 
        element:NewHooks,
        text:<><FaAccessibleIcon  /> <p> Learning new Hooks</p> </> , 
        to:"/learn/new Hooks"
    }
]

//Creating the array to estorage all pages
const pagesArray:RouteData[] = [
    {
        element:Home, 
        text:"Main Page", 
        to:"/"
    }, 
    {
        element:Page3,
        text:"Videos", 
        to:"/videos"
    },
    {
        element:Page4,
        text:"Learn", 
        to:"/learn",
        SubChild:SubChildsArray 
    }
]

export type Details = {
    author:string, 
    url:string,
    date:string | null , 
    hours?:string, 
    day?:string, 
    extra?:any,
}

export type Topic =Record<string, Details[] > ; 

export type Category = {
    CSS:Topic , 
    REACT:Topic, 
    HTML:Topic, 
}

export const Sources:Category= {
    CSS: 
    {
        "grid":[
            {
                "author":"Learndev",
                "url":"https://www.youtube.com/watch?v=eHaZlFcGl6k",
                "date":"25/11/2025", 
                "hours":"14:00", 
                "day":"Tuesday"
            }, 
            {
                author:"WebKitCoding", 
                url:" ", 
                date:"24/11/2025", 
                day:"Tuesday", 
                hours:"22:00", 
                extra:`The only thing i did was to create an aside elemetn, nothing more. 
                 and about the sideBarButton i just create an square input with a label, again nothing more
                * the main logic the useSideBar hook and the css file
                * The hook get a AsideRefernce using React.useRef<HTMLElement>(null), then it create 
                * a fuction that only toggle the current state, (it remove and add it at the same time...) ; 
                * and in the css file to work this property i only create a normal object like alwasy 
                * (eg. .SideBarContainer{background-color:white; }) but with the propetye fixed
                * and since we useSideBar hook only move and add the className word 'show'
                * when it is added it move to the lefth `
            }, 
            {
                author:"Slaying the dragon", 
                date:"28/11/2025", 
                url:"https://www.youtube.com/watch?v=EiNiSFIPIQE", 
            }

        ], 


        "position":[
            {   "author":"nova Designs ", 
                url:" https://www.youtube.com/watch?v=Sm1ORyc2Qao", 
                date:"23/10/2025", 
            }, 
            {
                author:"", 
                url:"https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position", 
                date:"31/11/2025", 
                day:"Monday", 
                hours:"9:00 hrs"
            }, 
            

            ], 
    
        "tailwindcss":[
            {
                author:"Tailwindcss_Documentation",
                url:"https://tailwindcss.com/docs/installation/using-vite ", 
                date:null
            }, 
        ]
    },


    REACT:{
        "Motivation":[
            {
                author:"Bro_Code", 
                url:"https://www.youtube.com/@BroCodez", 
                date:null
            }, 
            {
                author:"Evil_Learning_Code", 
                url:"https://www.youtube.com/watch?v=NdyWfdFr8Kg",
                date:null
            },] 
        , 
        "Libraries":[
            {
                author:"video.js", 
                url:"https://videojs.org/guides/react/", 
                date:"02-12-2025", 
                day:"Tuesday", 
                hours:"22:00hrs", 
                extra:"This is very starightfoward librari"
            }

        ], 

        "My_Stuffs":[
            {
                author:"Note", 
                url:"https://www.notion.so/React-2958186e429380749bf2d5b7db1a3eaf" , 
                date:null,
            }, 
        ]
        

    }, 

    HTML:{

    }
}


//creating contex to share the pages
export const  PAGES_CONTEXT: React.Context<RouteData[]>  = React.createContext( pagesArray ) ; 


//This will render all my website no 2 
export default  function App()
{
    const INFO:RouteData[] = React.useContext(PAGES_CONTEXT ) ; 
    const ASIDE_REF = React.useRef<HTMLElement>(null);
    console.log(Sources) ; 

    return (
        //This is my main Father Grid, it will handle the header,navBar,main,fotter
        <div 
        className="
        mainContent
        grid 
        grid-rows-[auto,1fr,minmax(15rem,auto)]


        

        min-w-[100vw]
        min-h-screen   m-0
        bg-[#EDE7DB]              
        dark:bg-neutral-910  
        dark:text-first   
      "
        >
        <NavigationContainer basename="/" >


            
            <PAGES_CONTEXT.Provider value={INFO}  >
                {/**First column  */}
                <Header  toggleSidebar={ASIDE_REF}
                className='flex flex-col gap-3 sticky top-0 bg-first h-20 w-full
                         dark:bg-gray-700 z-10 '  />
            </PAGES_CONTEXT.Provider>
            


            <SideBarContainer sideBarRef={ASIDE_REF} className="glass-effect dark-5  " >
                    <NavigationBar  information={SubChildsArray} className="nav-sidebar "   />
            </SideBarContainer>



















            {/**Second column  */}
             <NavigationRoutes information={INFO} />

            {/**Thrid column  */}
             <Footer className="dark-3 
        bg-fourth m-0 p-4 
        static
        z-10
        "  />
        </NavigationContainer>
        </div>
    )
}