export default function displayDate(date){
  var d = Date.parse(date);
  const DAY = 3600000 * 24;
  const monthNames = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
  ];
  const curr = Date.now();
  //handles full date
  if (curr-d >= DAY){
    let x = new Date(d);
    return (`${monthNames[x.getMonth()]}  ${x.getDay()}, ${x.getFullYear()}`);
  }
  else {
  //handles hours
  if(curr-d>3600000){
      let x = curr - d
      x = Math.round(x/3600000);
      return (`${x} hours ago`);
  }
  //handles mins and secs
  else {
    if(curr-d<=60000) {
      let x = curr - d;
      x = Math.round(x/1000);
      return (`${x} secs ago`);
    } else {
      let x = curr - d;
      x = Math.round(x/60000);
      return (`${x} mins ago`);
    }
  }

  }
}
