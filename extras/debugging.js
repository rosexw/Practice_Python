// function test1(a, b){
//     const x = test2(a, b)

//     const y = x + 5;
//     return y;
// }

// function test2(a, b){
//     return a + b;
// }

// underscore is i's value
// ['foo', 'bar', 'foobar', 'foobar2', 'foo', 'thing'].map((_, i)) => {
    // myObj.user.userAddr.streetNumber: 4333
['foo', 'bar', 'foobar', 'foobar2', 'foo', 'thing', {user: {userAddr: {streetNumber}}}].map((myObj, i)) => {
    if(i===14) {
        return i+10;
    } else {
        i + 5;
    }
}

// see global values
//myObj.user.userAddr.streetNumber

// const obj1 = {
//     foo: 'bar'
// };

// console.log(obj1);

// let obj2 = obj1;
// obj2.foo = 'zoobar';
// console.log(obj2);

// console.log(test1(5,70));

// debugger;
// debugging: break down line by line and can go back in time
// use in Chrome

// pause on breakpoints - you're not done the line, just starting the line - in, not assignment values
// console.log is great for things but not stopping step by step - have to watch order, but can't see how code is running. 
// Right click on line: Edit Breakpoint (to stop here only when x>50)

// call stack on chrome

// function test3(){
//     test2(8, test2(9,14));
// }

// test3(); // initiation of stack: now a = 9, b = 14 => 8, 23 => 31

// React, debugger: npm run start
// understand order of calling

// icons in debugger
// resume script = press to go to the next one or if last, stop debugging
// step over to next function call = go to next function
// step into next function call = go into function called and see what's happening
// step out of current function = rewind back
// step = go to next line executed in JS and see each line
// Deactivate = ignore breakpoints
// Pause on exceptions 

// null + 3 = 3
// return throw "oh no an error" ==> paused on exception
// main.js see exactly where error is occuring
// pause on caught exceptions - want to not ignore exceptions (try/catch)
// try {
//     const x = {}.foo.bar;
// } catch(err) {
//     console.log('oh no');
// }

// console.time()
// console.time('test 10000maps with index')
Array.from({length: 10000}).map((_, i) => {
    return (i + 1 + 1000 + 5) / 45 + "some string".length + 2)
});
console.timeEnd('test 10000 mpas with index');

// see how long process takes
 
// clock out - live debugger tool in your code