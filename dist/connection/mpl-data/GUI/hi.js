function run(){
    let {PythonShell} = require('python-shell');

    let options = {
        pythonPath: 'C:\\Users\\tomas\\Anaconda3\\python.exe',
    };

    PythonShell.run('Scraping.py', options, function (err, results){
        console.log(results);
        console.log('Python finished')
    })
}