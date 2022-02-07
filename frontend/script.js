


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
    const api_url = "https://api.moodify.tech/get?mood="+mood+"&genre="+genre
    const response = await fetch(api_url)
    const data = await response.json();
    console.log(data)
    //info = JSON.parse(data);
    info = data
    for (var i=0; i<info["songs"].length; i++) {
        const frame = document.createElement("iframe");
        frame.src = "https://open.spotify.com/embed/track/"+info["songs"][i]["id"]
        frame.width = 300
        frame.height = 380
        frame.frameBorder = 0
        frame.allowtransparency = true
        frame.allow = 'encrypted-media'
        console.log(i);
        document.getElementById("result").appendChild(frame)
    }
    //<iframe src="https://open.spotify.com/embed/album/1DFixLWuPkv3KT3TnV35m3" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
}
  



