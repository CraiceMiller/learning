import * as React from 'react';


export interface SideBarProps extends React.DetailedHTMLProps<React.HTMLAttributes<HTMLElement>, HTMLElement>  {
    sideBarRef:React.RefObject<HTMLElement | null> ; 
}

/**
 * 
 * @param param0 
 * @since 25 11 2025 at 23:25 hrs :(  
 * @returns 
 */
export const  SideBarButton = React.forwardRef<HTMLElement,SideBarProps>(
    ({className,sideBarRef },ref) => 
    {

    const Click_Handler = React.useCallback((event:React.MouseEvent<HTMLInputElement> )=>
    {
        const showName:string = "show" ; 
        const isChecked:boolean = event.currentTarget.checked ;
        const ListRef:DOMTokenList | undefined =  sideBarRef.current?.classList ; 
        if(ListRef !== undefined)
        {
            isChecked ? ListRef.add(showName ) : ListRef.remove(showName )  ; 
        }

        //console.log("The box was checked",isChecked)
  
    },[])

    return (
        <label>
            <input
            onClick={Click_Handler}
            className={`Input-SideBar ${className || ''} `}
             type='checkbox' />

            <div className='toggle' > 
                <span className="top-line common " ></span>
                <span className="middle-line common " ></span>
                <span className="bottom-line common " ></span>
            </div>
        </label>
    )
})




/**
 * @description The only thing i did was to create an aside elemetn, nothing more. 
 * and about the sideBarButton i just create an square input with a label, again nothing more
 * the main logic the useSideBar hook and the css file
 * The hook get a AsideRefernce using React.useRef<HTMLElement>(null), then it create 
 * a fuction that only toggle the current state, (it remove and add it at the same time...) ; 
 * and in the css file to work this property i only create a normal object like alwasy 
 * (eg. .SideBarContainer{background-color:white; }) but with the propetye fixed
 * and since we useSideBar hook only move and add the className word "show"
 * when it is added it move to the lefth 
 * @since i am here since 25 11 2025, at 15:00 to 00:00 : (, and i am writing this 
 * 
 */
export const SideBarContainer = React.forwardRef<HTMLElement, SideBarProps>(
    ({ children, className,sideBarRef,  ...rest },ref) => {
        return (
            <aside 
                className={`SideBarContainer ${className || ''}`}
                ref={ref || sideBarRef} 
                {...rest}
            >
                <h1 className="gradient-text text-purple-800 text-[6vw] font-poppins font-semibold mb-4 " >Menu</h1>
                {children}
            </aside>
        );
    }
);
