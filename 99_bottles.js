function bottleSong(int) {
    let numberOfBeers = int;
    let pluralWord = "bottles";
    let singularWord = "bottle";
for (i = numberOfBeers; i > 0; i--){
    
        if (i > 2){
            console.log(i + " bottles of beer on the wall, " + i + " bottles of beer");
            console.log("Take one down and pass it around, " + (i - 1) + " bottles of beer on the wall");
        }else if(i == 1){

            console.log(i + " bottle of beer on the wall, " + i + " bottle of beer");
            console.log("Take one down and pass it around, no more bottles of beer on the wall");
        }else{
            console.log(i + " bottles of beer on the wall, " + i + " bottles of beer");
            console.log("Take one down and pass it around, " + (i - 1) + " bottle of beer on the wall");
        }
        

}

  };
  
  bottleSong(4);