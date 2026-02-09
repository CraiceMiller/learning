//import React from "react";
import type { RouteData} from  "../utils/typing"; 
import { NavigationRoutes} from "../layouts/navBar"; 
import {MyPageFooter} from "../layouts/Footer"; 
import {MyPageHeader} from "../layouts/Header"; 
import {NavigationContainer,NavigationBar } from "@layouts/navBar" ; 
import App2 from "./website1/2";
import App3 from "./website1/3";
import App4 from "./website1/4";
import App5 from "./website1/5";
import App6 from "./website1/7";
import App8 from "./website1/8"; 
import App9 from "./website1/9"; 
import App10 from "./website1/10"; 
import App11 from "./website1/11"; //25 /10/25 - 2/11/2025
import App12 from "./website1/12"; //3/11/2025
import App13 from "./website1/13"; //8/11/2025
import P1 from "./failures/project1"; //24/10/2025
import '@styles/proyects.css' ; 
/**
 *
 */





export  class Page {
    static data:RouteData[] = []; 
    static data2:RouteData[] = []; 
    static data3:RouteData[] = []; 




    getData():RouteData[]{
        return Page.data
    }
    getData2():RouteData[]{
        return Page.data2
    }
    getData3():RouteData[]{
        return Page.data3
    }
    
    
    addData(...newData:RouteData[]):void{
       Page.data.push(...newData); 
    }
    addData2(...newData:RouteData[]):void{
        Page.data2.push(...newData); 
     }
     addData3(...newData:RouteData[]):void{
        Page.data3.push(...newData); 
     }
    
    
}

Page.prototype.addData(...[
    {
        to:"/app2", 
        text:"app 2", 
        element:App2 

    },

    {
        to:"/app3", 
        text:"app 3", 
        element:App3 

    },
    {
        to:"/app4", 
        text:"app 4", 
        element:App4

    }, 
    {
        to:"/app5", 
        text:"app 5", 
        element:App5 
    
    }, 
    {
        to:"/app6", 
        text:"app 6", 
        element:App6
    
    }, 
    {
        to:"/app8", 
        text:"app 8", 
        element:App8
    
    }, 
    {
        to:"/app9", 
        text:"app 9", 
        element:App9
    
    }, 
    {
        to:"/app10", 
        text:"app 10", 
        element:App10
    
    }, 
    
]
 )

Page.prototype.addData2(...[
    {
        to:"/proyect1", 
        text:"Table handaler", 
        element:P1
    
    }, 
    
 ])

 Page.prototype.addData3(...[
    {
        to:"/app11", 
        text:"a bunch of sttuff", 
        element:App11
    
    }, 
    {
        to:"/app12", 
        text:"learing new Hooks", 
        element:App12
    
    }, 
    {
        to:"/app13", 
        text:"Why this is happing to me :(", 
        element:App13
    
    }, 
    
 ])

export default function App(){
    return (
        <>
        <NavigationContainer >
            <MyPageHeader/> 
            <NavigationBar id="my-navigation"  information={Page.prototype.getData3().concat( Page.prototype.getData2()).concat(Page.prototype.getData())}/>
            <NavigationRoutes information={Page.prototype.getData3().concat( Page.prototype.getData2()).concat(Page.prototype.getData())} />
            <MyPageFooter/>
        </NavigationContainer>   
        </>   
    )
}
/**
 * 10/2025
 export default function App(){
    return (
        <>
     
       <MyPageHeader/> 
            
       <NavigationRoutes information={Page.prototype.getData3()} id="my-navigation" />
       <MyPageFooter/>
   </>   
)
}
*/

//console.log("Data: ", Page.prototype.getData())



