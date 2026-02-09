import {enumerate, all} from "../src/utils/utils.js" ; 
//import {callable} from "@myjs/utils.js" ;
import "./src/styles/myMess/myProperties.css" ;
import "@styles/index.css"; 
import "@src/styles/App.css" ;
import "@myjs" ; 
import type {PrimitiveValues } from  "@src/utils/typing.js" 
//import Button from "@src/components/buttons" ; 
//let a:string = 2 ; 

function fun(v:PrimitiveValues){
    console.log(v);
}

console.log('Trying to deggug this :(, start: 5/11/2025 at 16:30 ');
console.log("end: 6/11/2025 at 9:00 hrs ");

let v = [true,!0,2,"","Hello"]
console.log(all(v) ? 'yes':'no' );
for (let i of enumerate(v)){
    console.log(i);
}
console.log(fun("Bye world "));



/**
 05/11/2025
 # alias imports
 How to configure alias imports in ts
the only thing to do is go to your 'tsconfig.json' file and set both 
'baseUrl' and 'paths'
```tsconfig.json
{
    "compilerOptions":{
        "baseUrl":"./", 
        paths:{
            "@myfiles/*":["./mycarpet/sources/utils/myfiles/*"], 
        }
    }, 
}
```
and this is preety much it...
now we can use this alias in whatever file we want 
```myapp.ts
import {myfun} from "@myfiles/functions.ts" ; 
//instead of write the whole path
//import {myfun} from "./mycarpet/sources/utils/myfiles/functions.ts" ; 
```

## errors in the configurtion 
However it will be times that this does not work, therefore we need to 
do extras step to do it.
In our tsonfig.json we need to set up extra properties: 

```tsconfig.json
{
    "compilerOptions":{
        "baseUrl":"./", 
        paths:{
            "@myfiles/*":["./mycarpet/sources/utils/myfiles/*"], 
        }
    }, 
    // Tells TS to rely on the bundler (Vite) for module resolution.
    // This is key for non-relative path aliases to work correctly.
    "moduleResolution": "bundler",
    
    // Allows the compiler to look up paths without strictly enforcing import syntax.
    "verbatimModuleSyntax": false,
    
    // Needed if you explicitly import files with the .ts extension.
    "allowImportingTsExtensions": true,
}
```

and we need to add another properties in our another file 'tsconfig.app.json'
```tsconfig.app.json
{
    "compilerOptions"{
            "include": ["./mycarpet/sources/utils/myfiles/**  / *"], 
            "exclude": ["node_modules"],
            "extends":"./tsconfig.json",    
    }
}

```
however i still do not know why i need  to do this : |

## Explanations 
What the heck is going on here, is what are you wondering right now. well 
read the tex explanation below: 
PROPS IN tsconfig.json 
baseUrl: 
paths: 


Property,Explanation
"moduleResolution: ""bundler""",
"Why you need this for Vite: The default node module resolution often struggles with path aliases and requires the file extension in the import. Setting it to ""bundler"" tells TypeScript to trust the modern bundler (like Vite) to handle module lookups. This prevents TypeScript from throwing errors when it sees a non-relative path (@src/) that doesn't follow strict Node.js conventions."

verbatimModuleSyntax:false,
Why you need this (or why it causes issues): This is a very strict mode. Setting it to true demands that your import syntax exactly matches what's in the original file. Non-relative imports like aliases can sometimes fail this check. Setting it to false (or removing it) gives the compiler the flexibility needed for the alias path to resolve.

allowImportingTsExtensions: true,
"Why you need this (Optional but common): If you import a file with the .ts extension (e.g., import { fun } from ""@myfiles/functions.ts""), this flag is required to let TypeScript know those explicit extension imports are valid."

"extends: ""./tsconfig.json""",
"Why you need this in tsconfig.app.json: Since your project uses Project References (indicated by the references array in your root tsconfig.json), all the settings for your application (like paths) are usually defined in the root file. The tsconfig.app.json needs to explicitly inherit these settings via extends so the TS language server can see them when checking files inside src."

include,
"Why you need this in tsconfig.app.json: This tells the compiler which files to apply the configuration to. In a referenced project setup, if the file you are importing from (e.g., myfiles/functions.ts) is not listed in include, TypeScript may not process it, leading to the ""Cannot find module"" error."


exclude: 

## C. Runtime Fix (Vite Configuration)
Because a bundler like Vite doesn't automatically read tsconfig.json aliases for its build process, you must use the vite-tsconfig-paths plugin for synchronization.

Install: npm install -D vite-tsconfig-paths

Configure vite.config.ts:

```TypeScript

// vite.config.ts
import { defineConfig } from 'vite';
import tsconfigPaths from 'vite-tsconfig-paths';

export default defineConfig({
  plugins: [
    // ... other plugins ...
    tsconfigPaths(), // This plugin reads tsconfig.json and sets up Vite's aliases
  ],
  // DO NOT manually define aliases in resolve.alias when using this plugin
});
```

### Side notes
in our paths properties we write  "/*" at the end of the name to make it a folder, it will
be a file otherwise 
example: 
{
    "compilerOptions":{
        "baseUrl":"./", 
        paths:{
            "@myfiles/*":["./mycarpet/sources/utils/myfiles/*"], //this properties will act as a folder
            "@colors":["./Folder1/Folder2/CssStyles/uniques/darkColor.css"] //this will act as a file 
        }
    }, 
}
  
 */


