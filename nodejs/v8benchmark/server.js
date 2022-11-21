'use strict';

const express = require('express');
const cp = require('child_process');
const fs = require('fs');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();

var benchmarkFile = 'v8-v7/v8-v7.js';
var execComm = 'node ' + benchmarkFile;

app.get('/v8', (req, res) => {
  if (req.query.benchmark != undefined) {
    benchmarkFile = 'v8-v7/' + req.query.benchmark
    if (fs.existsSync(benchmarkFile )) {
      execComm = 'node ' + benchmarkFile;
    } else {
      res.send({message:'Benchmork model does not exist'});
      return;
    }
  } else {
    benchmarkFile = 'v8-v7/v8-v7.js';
    execComm = 'node ' + benchmarkFile;
  }
  
  cp.exec(execComm, (err, stdout, stderr) => {
    if (err) {
         console.log(err);
         res.sendStatus(500);
         return;
    }
    console.log('#1, exec');
    console.log(stdout);
    res.send({message:`${stdout}`});
})  
});

app.listen(PORT, HOST, () => {
  console.log(`Running on http://${HOST}:${PORT}`);
});