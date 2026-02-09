import type {Component} from "@utils/typing" ; 
import {SideBarContainer } from "@layouts/sideBar" ; 
import {NavigationBar } from "@layouts/navBar" ; 
import { Outlet} from "react-router-dom" ; 
//
import {SubChildsArray} from "@pages/website2" ; 
//start 24/11/2025 at 12:00 hrs , satruaday

//---->
export default  function App():Component
{

    return (
        <main className="

        "
        >
            {/**This one will re-render all my nested links */}
             <Outlet />
 
        
        {/**<MainContent />*/ }
        </main>
    )
}
/**min-h-dvh 
         grid-rows-[1fr_1px_auto_1px_auto] pt-26.25 lg:grid-cols-[var(--container-2xs)_2.5rem_minmax(0,1fr)_2.5rem] lg:pt-14.25 xl:grid-cols-[var(--container-2xs)_2.5rem_minmax(0,1fr)_2.5rem
*/