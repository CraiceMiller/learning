import {useRef, useEffect} from "react"; 
import videojs from 'video.js';
import "video.js/dist/video-js.css"; 
import type { VideoJsPlayer,  VideoJsPlayerOptions, VideoJsPlayerPluginOptions } from 'video.js'; 

//type VideoJSPlayer = ReturnType<typeof videojs>;
interface VideoTsProps 
{
    options:VideoJsPlayerOptions, 
    onReady?:(player:VideoJsPlayer)=>void , 
    className?:string; 
}




/**
 * @description This hook only use the library videojs to work with. you ease can modify the behavier of the 
 video using the options propertie, 

 *@prop {options} VideoJsPlayerOptions with this one you can change, modify and add diferent resource 
 to the video container. this could the source, caption, height, so on. 
 * @linbraries video.js@7.21.3 videojs-contrib-quality-levels@3.0.0 videojs-http-source-selector
 * --save-dev @types/video.js
 * @start 2/12/2025 Tuesday. 19:00hrs
 * @returns a video container
 */
 function VideoTs(props:VideoTsProps)
 {
    /**1. we set all varibles needed */
    const playerRef = useRef<VideoJsPlayer | null> (null) ; 
    const videoRef = useRef<HTMLDivElement | null>(null) ;  // to set the video itself
    const {onReady, options,className } = props ; //to handler the optiosn i guess 

    /**2. Now we settles all initial configuration  */
    useEffect(()=>
    {
        //if our player ref is not null then we update it right away. 
        if (playerRef.current) 
        {
            const player:VideoJsPlayer = playerRef.current;

            options.autoplay && player.autoplay( options.autoplay ) 
            options.sources &&  player.src(options.sources);
            return  ;  
        }
        //else we do the following configuration

        // The Video.js player needs to be _inside_ the component el for React 18 Strict Mode. 
            const videoElement:HTMLElement = document.createElement("video-js");
      
            //2.2 here just add the class vjs-big-play-centered class in the class list 
            //of the element we have been created :)
            videoElement.classList.add('vjs-big-play-centered');
            videoRef.current?.appendChild<HTMLElement>(videoElement);

            //2.3 lastly we create the constante player to pass as an argument to our onReady parameter
            //
            const player:VideoJsPlayer=videojs(videoElement, options, () => {
                onReady && onReady(player);
            });
            playerRef.current = player; 
            

    },[options,videoRef]) ; 


    // Dispose the Video.js player when the functional component unmounts
    // 3. here we are cleaning our code when unmounts 
    useEffect(() => {
        const player:VideoJsPlayer | null= playerRef.current;
        return () => {
        if (player && !player.isDisposed()) {
            player.dispose();
            playerRef.current = null;
        }
        };
    }, [playerRef]);

    return (
        <div className="w-full aspect-video"> 
            {/* The player div (videoRef) must fill the container */}
            <div ref={videoRef} className={` ${className || ''}`} >
                {/* VJS player is initialized here */}
            </div>
        </div>
    )

 }
 export default VideoTs ; 
 export type { VideoJsPlayer,  VideoJsPlayerOptions, VideoJsPlayerPluginOptions } ; 