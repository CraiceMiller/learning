const text = {
    status:'Error', 
    error:{
        text:'InvalidAPIKey', 
        halt:false, 
        status:'error',
        httpCode:500,
        httpReason:'Servererror',
        tag:null
    },
    info:{
        data:{
            fault:{
                faultstring:'invalid ApiKey for given resource',
                detail:{
                    errorcode:'oauth. v2. invalidapiKeyforGivenResource'
                }
            }
        },
        contentType:'application/json',
        responseClass:'data',
        encoded:false
    }

}

const info = {
    status:'Send',
    method:'POST',
    headers:{
        contentType:'application/json',
        responseClass:'data',
        encoded:false
    },
    detail:{
        text:'sending error json object',
        httpCode:200, 
        httpReason:'send',
        tag:null
    },
    message:'Sending data',
    body:JSON.stringify(text)

}

//let response = await fetch('https/0.0.1.01/API/data',info);

console.log(text);
console.log(info);