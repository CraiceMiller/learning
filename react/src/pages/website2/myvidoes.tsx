import React from "react"; 
import Videos from "@utils/database" ; 
import {toast, ToastContainer} from "react-toastify" ; 
import {useLocalStorage } from "@hooks/storages" ; 
import {CountDown} from "@components/count-down" ; 

//2/12/2025 TUESDAY 20:00
import type { VideoJsPlayer, VideoJsPlayerOptions }  from "@lib/videos" ; 
import VideoJS from "@lib/videos" ; 

export function Loading()
{
    return (
        <div className="loading 
        absolute top-1/2 left-1/2 translate-y-1/2 translate-x-1/2 " >
            <div className="span1" ></div>
            <div className="span2" ></div>
            <div className="span3 " ></div>

        </div>
    )
}

export interface SquareLinkProps extends React.AllHTMLAttributes<HTMLAnchorElement> 
{
    href:string ; 
    text: string ; 

}

export const SquareLink = ({href,text,className ,...rest}:SquareLinkProps ) =>(
    <a className={`justify-self-stretch px-[5px] pb-[10px]  
    visited:bg-purple-550 dark:visited:bg-purple-550
    active:bg-purple-550 dark:selection:bg-purple-700
    bg-gray-300 dark:bg-gray-800 hover:bg-purple-550 dark:hover:bg-purple-550
    relative
    `}   href={href} {...rest} target="_self"  >

             <p className=" absolute left-1/2  text-[1em] " >{text} </p>
    </a>
)



/**19/11/2025 */
export function BlockAreaEpisodes({handler}:{handler:React.Dispatch<React.SetStateAction<string>>})
{
    const ClickHandler = React.useCallback((event:React.MouseEvent<HTMLAnchorElement>)=>{
        event.preventDefault() ; 
          const url:string = event.currentTarget.href ;
          handler(url) ; 
//debugger ; 
    },[handler]); 

    const VideosDataBase: Record<string,string> = Videos.videos.animes.NazoNoKanojoX ; 
    let Episodes:React.JSX.Element[] = [] ; 
    /**React.useEffect(()=>
    {*/
        for (const key of Object.keys(VideosDataBase ) )
    {
        let currentEpisode:string | undefined = VideosDataBase[key ] ; 
        if (currentEpisode === undefined)break ; 

        Episodes.push(
            <SquareLink onClick={ClickHandler} href={currentEpisode} text={`${key}`} />
        )
    }

    /**},[])*/

    

    return (
        <section className="class_area block_area-episodes 
        pt-[5px] px-[15px] pb-[10px] mt-5
        rounded-[0.5rem] bg-gray-100 dark:bg-neutral-850"  >
          
                <div className="episodes-page-1 episodes-ul
                grid 
                grid-cols-[repeat(5,minmax(4vw,auto))] 
                auto-rows-[5vw] 
                text-[2vw]
                gap-[1vw] " >
                    {Episodes}
                </div>

        </section>
    )
}

/**20/11/2025*/
function Message()
{
    const videoUrl:string = React.useContext(VideoHrefContext) ;
    const VideosDataBase = Videos.videos.animes.NazoNoKanojoX ; 

    let r =  Object.values(VideosDataBase).findIndex((v,i)=>videoUrl===`http://localhost:5173/${v}`) ; 
    console.log(r)
    console.log(Object.values(VideosDataBase)) ; 
    console.log("current url: ", videoUrl) ; 
    
    return (
        <div className=" grid justify-center grid-cols-[2fr,1fr] gap-2 " >
            <div className="relative block " >
            <h1 className="font-dela-gothic-one text-[4vw] font-bold  hover:shadow-2xl   " >
                Nazo No Kanojo  </h1>
            <p className="font-poppins text-[1.9vw] " >You are currently watching Episode <strong>No.{ r } </strong>  </p>
            </div>

            <div className="relative " >
            <p className=" absolute top-[-14.5vw]  m-0 p-0 drop-shadow-2xl font-science-gothic text-[22vw] font-extrabold
                 text-purple-700 hover:shadow-2xl transition hover:translate-x-[5vw] " >
                x</p>
            </div>
        </div>
    )
}

/**19/11/2025 */
export function BlockVideoArea()
{
    //here i just get the current link video
     const videoUrl:string = React.useContext(VideoHrefContext) ; 

     //here is the videoJs configuration 
     const playerRef = React.useRef<VideoJsPlayer|null>(null);

     //here is the basic configuration 
     //it has the same like a normal video tag but even better
    const videoJsOptions:VideoJsPlayerOptions = {
        autoplay: false,
        controls: true,
        responsive: true,
        height: 50 ,
        fluid: true,
        tracks:[
            {
                kind:"captions", 
                label:"English", 
                language:"en", 
                default:true, 
                
            },
        ],
        sources: [{
        src: videoUrl,
        type: 'video/mp4'
        }, 
        ]
    };

    const handlePlayerReady = (player:VideoJsPlayer) => {
        playerRef.current = player;

        // You can handle player events here, for example:
        player.on('waiting', () => {
        console.log('player is waiting');
        });

        player.on('dispose', () => {
        console.log('player will dispose');
        });
    };

 
     
  
    /**npm  install --save-dev video.js@7.21.3 videojs-contrib-quality-levels@3.0.0 videojs-http-source-selector */

    return (
        <section className=" relative justify-self-stretch "  >
            
            {/**<video
             controls 
             src={videoUrl}
             key={videoUrl}  
            className=" block h-full w-[100%]  " >
                {/**here i need to add a subtilte file :| }
                <track kind="subtitles" srcLang="en" label="English :3" default />
                <track kind="subtitles" srcLang="es" label="Japanese :3"  />
            </video>*/}

            <VideoJS 
            options={videoJsOptions} 
            onReady={handlePlayerReady} />
        </section>
    )
}
/** 
interface VideoProps extends  React.MediaHTMLAttributes<HTMLVideoElement>{}
function video({className, src }:VideoProps )
{
    return (
        <section className={`video-component ${className || ''} `}  >
            <video
             controls 
             src={videoUrl}
            key={videoUrl}  
            className=" block w-100% " />
        </section>
    )

}
*/


const firstEpisodeUrl: string = Videos.videos.animes.NazoNoKanojoX[1];
const VideoHrefContext:React.Context<string>= React.createContext<string>(firstEpisodeUrl) ; 

/**
 * @start 18/11/2025
 * @update 2/12/2025 Tuesday at 18:00hrs. 
*/
function App()
{
    const [lastVideo, setLastVideo] = useLocalStorage('lastVideo',firstEpisodeUrl) ; 
    const [urlVideo,setUrlVideo] = React.useState<string>(lastVideo ) ;
    React.useEffect(()=>{
        setLastVideo(urlVideo) ; 
        
    },[urlVideo]) ; 
    return (
        <main className="mx-[5vw] grid grid-rows-[repeat(5,minmax(10rem,auto))] " >
            <VideoHrefContext.Provider value={urlVideo}  >
                <Message/> 
                <BlockVideoArea />
                <BlockAreaEpisodes handler={setUrlVideo} />
                
                <CountDown 
                seconds={7}
                id="countdown"
                className=""
                 onFinish={()=>{
                    toast("The counter finished") 
                    const div = document.querySelector<HTMLDivElement> ("#countdown") ; 
                    if(!div)return ; 
                    div.style.scale = "0" ; 
                    }}  />
            </VideoHrefContext.Provider>
            <ToastContainer/>
        </main>
    )
}
export default App ; 