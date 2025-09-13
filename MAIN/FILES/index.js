const scroll = new LocomotiveScroll({
    el: document.querySelector('.main'),
    smooth: true,
    // multiplier:0.1
    lerp:0.04
});
function updateClock() {
  let options = { 
    timeZone: "Asia/Kathmandu", 
    hour: '2-digit', 
    minute: '2-digit', 
    second: '2-digit',
    hour12: false   // force 24-hour format
  };
  let formatter = new Intl.DateTimeFormat([], options);
  document.getElementById("clock").textContent = formatter.format(new Date());
}
  updateClock(); // show immediately
  setInterval(updateClock, 1000); // update every second
