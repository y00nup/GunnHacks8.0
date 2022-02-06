


mood = ""
genre = ""
function setmood(selmood) {

    mood = selmood
    console.log("mood = " + mood)
}

function setgenre(selgenre) {
    genre = selgenre
    console.log("set genre to "+ genre)

}




async function getData() {
    const api_url = "https://GunnHacks80.agastyasandhuja.repl.co/get?mood="+mood+"&genre="+genre
    console.group(api_url)
    const response = await fetch(api_url)
    const data = await response.json();
    
}
  



