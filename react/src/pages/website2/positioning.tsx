import React from "react" ; 
import {CreateItem, CreateSlot, SwapyContainer } from "@lib/swap" ; 
import {ErrorBoundary } from "@hooks/react-utils" ; 


/**
 
 * <dl> is the wrapper father to handle all the text
* <dt> is for tittles
 * <dd> is for text 
 * @since 31/11/2025
 */
function MY_INFORMATION_TEXT(){
    return (
        <CreateItem itemName="Text-information"  >
            <dl>
            <dd>
                <p>
                it is use to contorl the position of a n elemetn on a <strong> web page</strong>. 
                </p>
                <p>
                The position in css are very important to create respoinsive and beaiful website taht looks like
                appealing to the viewever. There are five main categories at hand [static,relative,absolute,fixed,sticky]. 

                The majority of the position we can manipulate usignt the properties
                <ul>
                    <li>top</li>
                    <li>right</li>
                    <li>bottom</li>
                    <li>left</li>
                </ul>
                </p>
                <hr/>
            </dd>
            <dt>
                <h3>Staitic</h3>
            </dt>
            <dd>
                <p>
                    The default value, elements are position according to the nomal flow of the document 
                </p>
                <p>
                this is the easy one, due all the HTML elements as a default have static positon, meaing it take one posite aside
                from another children withtin a father. 
                </p>
            </dd>
            <dt>
                <h3>Relative</h3>
            </dt>
            <dd>
                <p>
                    Moves the element relative to the normal postion.
                </p>
                <p>
                The same as static, it has their own space, but with the differnt I can move its position using the properties 
                <ul>
                    <li>top</li>
                    <li>right</li>
                    <li>bottom</li>
                    <li>left</li>
                </ul>
                </p>
            </dd>
            <dt>
                <h3>Absolute</h3>
            </dt>
            <dd>
                <p>
                This remove the element from their space  And we can move it inside the father
                </p>

            </dd>

            <dt>
                <h3>Fixed </h3>
            </dt>
            <dd>
                <p>
                    It follow the same four properties, top bottom right left, but this time it 
                    is remove from all the father and grandfather, and its father becoms the HTML tag
                    or the window itself. 

                </p>
            </dd>

            <dt>
                <h3>Stcky </h3>
            </dt>
            <dd>
                <p>
                    This position remains in its place but, when the window reach to one of these properties 
                    top,right,bottom, left, it become fixed to it...

                </p>
            </dd>

            <dd>
                <p>
                in short, all elements in html have thier unique space, since everyone has static as a default. here is when we use position: 

common: 

relative,absolute,fiexed,sticky we can use the properties top,right , bottom, left



difference: 

static, sticky,relative does not lose their places.

fixed, absolute lose their places. 

fixed looks from the viewport. 

absolute looks from the nearest relative father, if there is no any goes from the viweport.



i like to see like the messuare i learn yesrsteday: 

2rem = the number multiply by the viewport html tag,16 as a default. 

2em = the number mulply by the nearest father with size, if there is no any, goes from the viwport
                </p>
            </dd>

 

            


        </dl>
        </CreateItem>
        
    )
}



function Boxes(){
   return (
    <>
    <div className="Box Fixed glass-effect " >Box I <br/> Fixed </div>
    <div className="Box Relative" >Box II <br/> Relative </div>
    <div className="Box Absolute" >Box III <br/> Absolute</div>
    <div className="Box Sticky" >Box IV <br/> Sticky</div>
    <div className="Box Static" >Box V <br/> Static</div>

    </>
   )
}

function PositionGrid()
{
    return (
        <div className="Container-Grid">
            <Boxes />
        </div>
    )
}
function PositionFlex()
{
    return (
        <div className="Container-Flex">
         <Boxes/>
        </div>
    )
}



export function Title()
{
    return (
        <CreateItem className="  grid grid-cols-[auto,1fr] gap-x-6 justify-items-center items-center " itemName="Title-item" >
            <div>
                <h1 className=" font-science-gothic 
                font-black  italic  text-[8vw] " >Position</h1>
                <hr/>
            </div>
            <div>
                <p className=" font-raleway font-thin text-4xl " >
                    Is it the way we arrange elements based in the space of a father or the html itself
                  </p>
            </div>
        </CreateItem>
        
    )
}


export default function App()
{
    return (
        <ErrorBoundary fallback="Something goes wrong" >
             <SwapyContainer className="
        grid 
        grid-rows-[auto,minmax(20rem,auto),auto]
        grid-flow-row
        gap-y-7
        mx-[5vw]

        " >
            <CreateSlot slotName="slot-1" >
                <Title />
            </CreateSlot>
            <CreateSlot className=" glass-effect Container-positions" slotName="slot-2" >
                <CreateItem  itemName="Positions" >
                    <PositionGrid />
                     <PositionFlex />
                </CreateItem>
            </CreateSlot>
            <CreateSlot slotName="slot-3" >
              <MY_INFORMATION_TEXT />
            </CreateSlot>
        </SwapyContainer>

        </ErrorBoundary>
       
    )
}