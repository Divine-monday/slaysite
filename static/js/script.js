//A tab single page containing the headers without linking to other pages.
const tabs = document.querySelectorAll("[data-tab-target]")
const tabContents = document.querySelectorAll("[data-tab-content]")

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    const target = document.querySelector(tab.dataset.tabTarget)
    tabContents.forEach(tabContent => {
      tabContent.classList.remove('active')
    })
    target.classList.add('active')
  })
})



var btt =document.getElementById('back-to-top'),
		body =document.body,
		docelen = document.documentElement,
		offset = 100,
		scrollpos,docheight
		// isbrowser = navigator.userAgent.toLowerCase().indexOf('edge') > -1,


		// calculate document height

		docheight = Math.max(body.scrollHeight, body.offsetHeight,docelen.clientHeight, docelen.scrollHeight, docelen.offsetHeight)	
		if (docheight !=  undefined) {
			offset = docheight / 7 ;
		}

		console.log(offset)
		// add scroll event

		window.addEventListener('scroll',function(event){
			scrollpos = body.scrollTop || docelen.scrollTop;
			console.log("position",body.scrollTop)
			btt.className = (scrollpos > offset) ? 'visible' : '';
		});

		// add click event
		btt.addEventListener('click',function(event){
			event.preventDefault();
			console.log("clicked")
			body.scrollTop = 0;
			docelen.scrollTop = 0;
			// if (isbrowser){
			// 	docelen.scrollTop = 0;
			// 	body.scrollTop = 0;
			// }else{
			// 	body.scrollTop = 0;
			// }
		});