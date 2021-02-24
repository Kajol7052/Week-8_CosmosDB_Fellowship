{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 function createToDoItems(items) \{\
    var collection = getContext().getCollection();\
    var collectionLink = collection.getSelfLink();\
    var count = 0;\
\
    if (!items) throw new Error("The array is undefined or null.");\
\
    var numItems = items.length;\
\
    if (numItems == 0) \{\
        getContext().getResponse().setBody(0);\
        return;\
    \}\
\
    tryCreate(items[count], callback);\
\
    function tryCreate(item, callback) \{\
        var options = \{ disableAutomaticIdGeneration: false \};\
\
        var isAccepted = collection.createDocument(collectionLink, item, options, callback);\
\
        if (!isAccepted) getContext().getResponse().setBody(count);\
    \}\
\
    function callback(err, item, options) \{\
        if (err) throw err;\
        count++;\
        if (count >= numItems) \{\
            getContext().getResponse().setBody(count);
        \} else \{\
            tryCreate(items[count], callback);\
        \}\
    \}\
\}}
