import React from "react"; 
import * as Swapy from "swapy" ; 
import type {ItemProps,SlotProps,useSwapyProps,SwapyContainerProps } from "./types/typing"
/**
 * 12/11/2025 at 20:00 hrs
 * The library Swapy is very useful to create dragrable objects to differents elemetns
 * 
 */
//12/11/2025 swapy 

/**
 * Renders a draggable item element, applying the necessary Swapy data attribute.
 * This component should generally be placed inside a CreateSlot component.
 * * @param {ItemProps} props - The properties for the item component.
 * @returns {React.JSX.Element} A div element marked with data-swapy-item.
 */
export function CreateItem({className,children,itemName,...rest}:ItemProps):React.JSX.Element
{
    return (
        <div
        className={`Item-Container  ${className}`} 
        data-swapy-item={itemName}
        {...rest}
        >
            {children}
        </div>  
    )
}
/**
 * Renders a slot element, applying the necessary Swapy data attribute.
 * The content (an item) can be provided either via the 'children' prop (preferred)
 * or dynamically generated using 'itemIside' and 'itemProps'.
 * * @param {SlotProps} props - The properties for the slot component.
 * @returns {React.JSX.Element} A section element marked with data-swapy-slot.
 */
export function CreateSlot(props:SlotProps):React.JSX.Element
{

    const { className, slotName, children, itemIside, itemProps } = props;
    let contentToRender;

    if (children) {
        contentToRender = children;
    } else if (itemIside && itemProps) {
        contentToRender = (
            <CreateItem 
                className={itemProps.className} 
                children={itemProps.children} 
                itemName={itemProps.itemName}
                // Pass any other itemProps down
                //{...itemProps} 
            />
        );
    }
    return ( 
        <section
            className={`Slot-Container ${className || ''}`} 
            data-swapy-slot={slotName}
        >
            {contentToRender}
        </section>
    );
}

/**
 * create a generic temple to storage one single container (like a list), but 
 * with the function that swap has. i planed to create based on the useEffect, 
 * useRef, useState React hooks
    -It must contain a swap event props as  a callback
    -it must containt the number of slots 
    - it must containt the containt of the slots, (based on the user provided)
    - it must

    my idea: 
        <useSwapy
        swapyEvent={(event:SwapEvent)=>{}}
        noSlots={4}
        slotprops={{}}
        items={{

        }}
        />

    pesudo: 
        section className=container:
            for noSlots times do: 
                div data-swapy-slot=slotprops.slotName className=slotprops.className : 
                    if wantitem do : 
                        div data-swapy-item=itemprops.slotName className=itemprops.className: 
                        end div
                    else : 
                        empty
                    end if 

                end div 
            end for 
        
        end section 

 */

/**
 * A custom React hook to initialize and manage the Swapy instance on a DOM element.
 * It ensures the library is set up once on mount and properly destroyed on unmount.
 *
 * @param {useSwapyProps} props - Configuration and event handlers for the Swapy instance.
 * @returns {[React.RefObject<HTMLDivElement | null>, Swapy.Swapy | null]} An array containing the ref object to attach to the container and the initialized Swapy instance (or null if not yet mounted).
 */
export function useSwapy(props:useSwapyProps):[React.RefObject<HTMLDivElement | null> ,Swapy.Swapy | null]
{
    const SWAPY_CONTAINER: React.RefObject<HTMLDivElement | null>  = React.useRef<HTMLDivElement|null>(null) ; 
    const [swapyInstance, setSwapyInstance] = React.useState<Swapy.Swapy | null>(null);
    const handlers = React.useMemo(() => ({
        onSwapy: props.onSwapy,
        onSwapyStart: props.onSwapyStart,
        onSwapBefore: props.onSwapBefore,
        onSwapEnd: props.onSwapEnd,
        config: props.config,
    }), [
        props.onSwapy, 
        props.onSwapyStart, 
        props.onSwapBefore, 
        props.onSwapEnd, 
        props.config
    ]);

    React.useEffect(() => {
        const value = SWAPY_CONTAINER.current;
        if (value === null) return;

        // 3. Create the swapy object
        const SWAPY = Swapy.createSwapy(value, handlers.config);
        SWAPY.enable(true);
        setSwapyInstance(SWAPY);

        // 4. Handler the events using the stable handlers object
        handlers.onSwapy && SWAPY.onSwap(handlers.onSwapy);
        handlers.onSwapyStart && SWAPY.onSwapStart(handlers.onSwapyStart);
        handlers.onSwapBefore && SWAPY.onBeforeSwap(handlers.onSwapBefore);
        handlers.onSwapEnd && SWAPY.onSwapEnd(handlers.onSwapEnd);
        
        // Final cleanup
        return () => {
            SWAPY.destroy();
        };

    // 5. Dependency array is clean: only the ref value and the stable handlers object
    }, [SWAPY_CONTAINER.current, handlers]);

    return [SWAPY_CONTAINER,swapyInstance] ; 

}

/**
 * A container component that utilizes the useSwapy hook to enable drag-and-drop 
 * functionality for its children (which should be CreateSlot components).
 *
 * @param {SwapyContainerProps} props - Props for the container, including Swapy event handlers and configuration.
 * @returns {React.JSX.Element} A div container with the necessary ref attached for Swapy initialization.
 */
export function SwapyContainer({children,className,...useSwapyProps}:SwapyContainerProps):React.JSX.Element
{
    const [SWAPY_CONTAINER,swap] = useSwapy(useSwapyProps)
    
    return(
        <div {...useSwapyProps} ref={SWAPY_CONTAINER}  className={`Swapy-Container ${className || ''}`} >
            {children}
        </div>
    )
}

interface  P extends  ItemProps , SlotProps {} ;
export function SlotItem(props: P )
{
    return (
        <CreateSlot  slotName={props.slotName} >
            <CreateItem itemName={props.itemName} >
                {props.children}
            </CreateItem>
        </CreateSlot>
    )
}

