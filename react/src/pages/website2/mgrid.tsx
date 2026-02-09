import React from "react" ; 
import type {Component} from "@utils/typing" ; 
import { Card} from "@components/cards" ; 
import {SwapyContainer,  SlotItem , CreateItem, CreateSlot} from "@lib/swap" ; 
import {Form } from "@components/choices" ;  
import type { FormProps} from "@components/choices" ;  


//
function calculateVp(windowSize:number,elementVp:number):number{
    return windowSize * (elementVp / 100 ) ; 
}

function useDisplaySizePort(elementVp:number,kind:'width'|'height',elementKind?:string ):void
{

    const windowSize =()=> kind === 'width' ? window.innerWidth : window.innerHeight ; 

    React.useEffect(()=>
    {

         const update = ()=>{
              
            const CurrentElementsize = calculateVp(windowSize() ,  elementVp ); 
            console.log(`The Window <<${kind}>> is: ${windowSize() } ` ) ; 
            console.log(`The ${elementKind || 'Element' } Size is: ${CurrentElementsize} ` ) ; 

        } ; 

   
        window.addEventListener("resize",update ) ; 

        return ()=>{
            window.removeEventListener("resize",update ); 
        }

    },[])
}


//24/11/2025
const CHARACTERS:Record<string,{name:string,url:string}> = {
    1:{
        name:"Mikoto Urabe", 
        url:"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCoMrUv1e67frBr1XOTW9vo8YZgdvpcB736w&s"
    },
    2:{
        name:"Akira Tsubaki",
        url: "data:image/jpeg;base64,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 "    },
    3:{
        name:"Ayuko Oka ", 
        url:"data:image/jpeg;base64,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"
    }
    ,
    4:{
        name:"Kouhei Ueno ", 
        url:"data:image/jpeg;base64,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"
    },
    5:{
        name:"Aika Haykawa ", 
        url:"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScJPTz1S8wR2NZvvRfVFi-XVRwdj6bfCpL6g&s"
    }
    ,
    6:{
        name:"Momoka Imai", 
        url:"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREr3TW3ck7eDlBGCZ8cZQb2Q1d__waOx8VhzdcZWCkMkDMWEcsh04iqgCrOqjpvIqlF3A&usqp=CAU"
    }

}

function FormLarge({onSend,className,...rest}: Omit<FormProps,"text"> )
{
    const [value,setValue] = React.useState<string>('') ; 
    const ChangeHandler = (event:React.ChangeEvent<HTMLTextAreaElement> )=>{
        const currentValue = event.currentTarget.value ; 
        setValue(currentValue ) ; 
    }

    const SendHandler = (event:React.FormEvent)=>{
        event.preventDefault() 
        onSend(value) ; 
    }

    return (
        <form className={className}  onSubmit={SendHandler} {...rest} >
            <textarea value={value} onChange={ChangeHandler } >

            </textarea>
        </form>
    )
}

function MyGrid():Component
{
    let listCard:React.JSX.Element[] = [] ; 

    const Create = ({url,name}: {url:string,name:string})=>(
        <Card className='min-h-[5rem] min-w-[5rem] bg-gray-300 shadow-xl dark:text-black cursor-pointer'  Imgsrc={url} Title={name}  />
    )

    for (const char of  Object.values( CHARACTERS) ) 
    {
        listCard.push( 
            <SlotItem itemName={`Item-${char.name}`} slotName={`Slot-${char.name }`} >
                <Create name={char.name} url={char.url}  />
            </SlotItem>
        )
        
    }

    return (
        <div className="text-center" >
            <h1>Characters </h1>
                <SwapyContainer 
                className="
                mx-36 grid  
                grid-cols-[repeat(3,minmax(100px,auto))]
               /** grid-rows-[repeat(2,minmax(5rem,15rem))]*/
                content-between
                


               
               
                

            
                gap-x-6
                gap-y-2
                 " >
                    {listCard}
            </SwapyContainer>
        </div>
    )
} 

function MyGrid2():Component
{
    let Divs = [] ; 
    for (let i:number = 1 ; i <= (5*5);i++)
    {
        Divs.push(
            <CreateSlot
            className="bg-gray-200  rounded-sm 
            shadow-lg
            
            hover:cursor-pointer h-20 w-20 " 
            slotName={`slot-${i}`} >

                <CreateItem className="bg-indigo-900 h-full w-full " itemName={`item-${i}`} >
                    {i}
                </CreateItem>
            </CreateSlot>

        )
    }

    return (
        <div className="text-center" >
            <h1>Practicing Griding here  </h1>
            <p>25 11 2025 </p>
                <SwapyContainer
                className="
                mx-36 grid  
                grid-cols-[repeat(5,minmax(7rem,auto))]
                grid-rows-[repeat(5,minmax(7rem,auto))]

                justify-items-center
                items-center
                 " >
                    {Divs}
            </SwapyContainer>
        </div>
    )
} 

function MyGrid3():Component
{
    function getSizeWidth ():number{
        return window.innerWidth ; 
    }; 

    const [width,setWidth] = React.useState<string>('') ; 
    const textVw :number = 5; 
    //useDisplaySizePort( textVw, "width", 'H1') ; 
    React.useEffect(()=>
    {
        const update = ()=>setWidth(()=>{
            const currentwidth = getSizeWidth() ; 
            const currentTextSize = calculateVp(currentwidth,textVw ); 

            return `Window Width Size:${currentwidth}px. Text Size:${currentTextSize }px  ` ; 

        } ) ; 
        

        window.addEventListener("resize",update ) ; 

        return ()=>{
            window.removeEventListener("resize",update ); 
        }
    },[])

    return (
        <div className="text-center  grid grid-rows-[5rem,mimax(10rem,auto)] gap-y-9 " >
            <div  >

                <h1 className={`text-[${textVw}vw]`} >- Practicing Gridding Positon - vw </h1>
                <h1 className={`text-[${textVw}rem]`} >- Practicing Gridding Positon - rem </h1>
                <div className="text-[1vw] h-28 " >
                    <h1 className={`text-[${textVw}em]`} >- Practicing Gridding Positon - em </h1>
                </div>
                <h1 className={`text-[${textVw}px]`} >- Practicing Gridding Positon - px </h1>

                <p  >27 11 2025  at 9:00hrs Friday</p>
                <p  >text viewportWidth: {textVw }  </p>
                <p> { width} </p>
            </div>
            
                <SwapyContainer
                className="
                mx-36 grid  
                grid-cols-[15rem,minmax(20vw,auto)]
                grid-rows-[7rem,10rem,minmax(10vw,auto),15vw]

               justify-center
                gap-x-6
                gap-y-2
                 " >

                <CreateSlot className="
                relative
                bg-gray-400
                rounded-sm
                hover:cursor-pointer
                h-full w-full " slotName={`slot-100`} >

                    <CreateItem className="h-full w-full bg-blue-900 "  itemName={`item-100`} >
                        {100}
                    </CreateItem>
               </CreateSlot>

               

               <CreateSlot className="
               row-span-2

                bg-gray-400
                rounded-sm
                hover:cursor-pointer              
                " slotName={`slot-101`} >

                    <CreateItem className="h-full w-full bg-blue-900 "  itemName={`item-101`} >
                        {101}
                    </CreateItem>
               </CreateSlot>

               <CreateSlot className="
                bg-gray-400
                rounded-sm
                hover:cursor-pointer
               
                 " slotName={`slot-102`} >

                    <CreateItem className=" bg-blue-900 "  itemName={`item-102`} >
                        {102}
                    </CreateItem>
               </CreateSlot>

               <CreateSlot className="
                bg-gray-400
                rounded-sm
                hover:cursor-pointer
                h-[7rem] w-[7rem] " slotName={`slot-103`} >

                    <CreateItem className="h-full w-full bg-blue-900 "  itemName={`item-103`} >
                        {103}
                    </CreateItem>
               </CreateSlot>
               <CreateSlot className="
                bg-gray-400
                rounded-sm
                hover:cursor-pointer
                h-[7rem] w-[7rem] " slotName={`slot-104`} >

                    <CreateItem className="h-full w-full bg-blue-900 "  itemName={`item-104`} >
                        {104}
                    </CreateItem>
               </CreateSlot>

               <CreateSlot className="
                col-span-2
                bg-gray-400
                rounded-sm
                hover:cursor-pointer
                 " slotName={`slot-200`} >

                    <CreateItem className="h-full w-full bg-blue-900 "  itemName={`item-200`} >
                        {200}
                    </CreateItem>
               </CreateSlot>

            </SwapyContainer>
        </div>
    )
} 
function MyGrid4():Component
{
    //const [justify,setJustify] = React.useState<string>("") ; 

     const justify = "justify-items-center justify-center " ; 
    return (
        <div className="text-center  mx-36 grid grid-rows-[15rem,repeat(2,minmax(15rem,auto))] gap-y-9 " >
            <div className="grid grid-cols-[auto,1fr] justify-items-center items-center gap-x-4   "  >
                <div>
                    <h1 className={`text-[7vw] m-0 gap-0 font-extrabold border-b-2 `} > Align <br/> Properties </h1>
                    <p> 27/11/2025  </p>
                </div>
                <div className="text-justify" >
                    < p className="text-sm" >This is just <strong> plain grid </strong>  , using grid are in order to understand more regards the layout in css and react. I guess this so simple but i dunno Why i keep failling over and over again :(  </p>
                        {/**<FormLarge className="text-black bg-transparent " onSend={v=>setJustify(v) } />*/}
                    
                    <br/>
                    <hr/>
                    <ul>
                        <li><p>justify-content</p> </li>
                        <li><p>justify-items</p> </li>
                        <li><p>align-content</p> </li>
                        <li><p>align-items</p> </li>
                    </ul>
                    

                </div>
            </div>

            <section
                className={`flex ${justify} `} >

                <div className="
                bg-green-900
                hover:cursor-pointer
                 " >
                    <h3>Header</h3>
                    <p>Some text</p>
                    <button>My Button </button>
               </div>
               <div className="
               block
                bg-purple-900
                hover:cursor-pointer
                " >
                    <h3>Main</h3>
                    <p>This is it </p>
                    <div>1</div>
               </div>
               <div className="
                bg-gray-500
                hover:cursor-pointer
                 " >
                    Footer
               </div>


               

            
            </section>
            
            <section
                className={`
                 grid  
                grid-cols-[repeat(3,minmax(10rem,auto))]
                grid-rows-[repeat(2,minmax(10rem,auto))]

                ${justify} 

                 `} >

                <div className="
                bg-green-900
                hover:cursor-pointer
                 " >
                    <h3>Header</h3>
                    <p>Some text</p>
                    <button>My Button </button>
               </div>
               <div className="
               inline-block
                bg-purple-900
                hover:cursor-pointer
                px-4
                " >
                    <h3 className=" hover:bg-white" >Main</h3>
                    <p className=" hover:bg-white" >This is my text that should content all the main infromation at hand, however idduon why i keep a
                    like this it is weir strange and anoyying ... </p>
                    <div className=" hover:bg-white" >1</div>
               </div>
               <div className="
                bg-gray-500
                hover:cursor-pointer
                 " >
                    Footer
               </div>


               

            
            </section>
        </div>
    )
} 


/**
 

# MESSAURE: 
27/11/2025
when we talk about size, we are refering to the font-size property,text-[],  
- vw
- vh
- rem 
- em 
- px
- 

vh vw: these one are wiewPort width|height, the window , I see this one like a rezise window event. 
this one is calculate based of the current window width|height. if the current window size is 1366px then the element of 5vw would be 68.3px. it could be calculated using this formula: 
   vw/vh (x) =  window.width|height * ( number / x ) 

rem: This is calculated based on the size of the <HTML> tag in our HTML file. as a defautl this one has a size of 16px, meaning all our element using the rem woulb be multiply by the html size 

rem  (x) = HTML.size * x 
16 * 5 = 80px

em: it is the same as rem but using the father size instead, if father has no size, it look throughout all parents, if no one parents has a size, it will be the HTML size again.
em (x) = Father.size * x ; 
div = 20px
h1 = 2em
20 * 2 = 40px

------------------------------------------------------------------------------------------------------

Grid
Father properties:
    display: grid
    grid-template-rows
    grid-template-columns
    grid-template-areas
    gap
    justify-content //this i dunno 
    align-content //and this i dunno what they do :( 
    grid-row-start grid-row-end
    grid-row

Child properties: 
    grid-area
    grid-row
    grid-colum

Tailwind: 
father: 
    grid
    grid-cols-2
    grid-rows-2

    gap-2
children: 
    col-span-1
    row-span-1


------------------------------------------------------------------------------------------------------
# Properties: 
justify-content:This controls how items are aligned along the main axis, father, (horizontal by default) this one only arrange the father itself, where the div(section,main,so on) could be. It would be: 
    - flex-start: moves all elements in the left 
    - center:it moves all elements in the center in X direction 
    - flex-end: moves all elements in the right 
    - space-between: it create a gap to all the elements, in order to fill the X direction space
    - space-around: the same to betwee, but it create an extra gap in the firts and last element. 
Tailwind: 
    justify-start
    justify-center
    justify-end
    justify-between 
    justify-around

align-items: this controls how itmes are aligned along the cross axis (vertical by default) within their lines  this will modify all the children inside the father
It would be: 
    - flex-start: moves all elements in the left 
    - center:it moves all elements in the center in Y direction 
    - flex-end: moves all elements in the right 
    - stretch: it will fill all the abivalby Y direction space
Tailwind: 
    items-start
    items-center
    items-end
    items-stretch

justify-items(only fro grid): this sets the alignments all items along the inline horizontal axis their grid area. the same as justify-content but for children  within their own lines (space). 
Tailwind: 
    justify-item-start
    justify-item-end



------------------------------------------------------------------------------------------------------


 * @returns 
 */
export default function App()
{
    return (
        <div className="
        grid 
        gap-y-7
        " >
            <MyGrid />
            <MyGrid2 />
            <MyGrid3 />
            <MyGrid4 />
 
        </div>
    )
}