const seat=document.querySelector('.seat');
const seat1=document.querySelectorAll('.rob .seat1:not(.occ)');
const count=document.getElementById('gound');
const total=document.getElementById('dotal');
const movieselect=document.getElementById('select');

populateUI();

let ticketPrice= +movieselect.value;

//saveselected movietype and price
function setmoviedata(movieIndex, movieprice) {
    localStorage.setItem('selectedMovieIndex', movieIndex);
    localStorage.setItem('selectedMoviePrice', movieprice);
}




function updateselectedcount() {
    const selectedseats=document.querySelectorAll('.rob .seat1.info3');
    

    const seatsIndex= [...selectedseats].map(function(seat) {
        return [...seat1].indexOf(seat);
    });
    
    localStorage.setItem('selectedseats',JSON.stringify(seatsIndex));

    const selectedseatscount=selectedseats.length;
    count.innerText=selectedseatscount;
    total.innerText=selectedseatscount*ticketPrice;
}

function populateUI() {
    const selectedseats=JSON.parse(localStorage.getItem('selectedseats'));

    if(selectedseats !== null && selectedseats.length > 0) {
        seat1.forEach((set, index) => {
            if(selectedseats.indexOf(index) > -1){
                set.classList.add('info3');
            }
        })
    }

    const selectedMovieIndex = localStorage.getItem('selectedMoviesIndex');
    if(selectedMovieIndex !=null){
        movieselect.selectedIndex = selectedMovieIndex;
    }
}

//type select event
movieselect.addEventListener('change', e => {
    ticketPrice= +e.target.value;
    setmoviedata(e.target.selectedIndex, e.target.value);
    updateselectedcount();
});

seat.addEventListener('click', (e) => {
    if(e.target.classList.contains('seat1') && !e.target.classList.contains('occ')){
        e.target.classList.toggle('info3');
    }

    updateselectedcount();
});
updateselectedcount();
let button=document.getElementById('bton');
button.addEventListener('click', (e) =>{
    if(count.innertext !=0){
        let bookings_details={
            'quantity':count.innertext,
            'amount':total.innertext,
        }
    fetch('/ooota_kannadi',{
        method :'POST',
        credentials : 'same-orgin',
        headers : {
            'Accept':'application/json',
            'X-Requested-With':'XMLHttpRequest',
            'X-CSRFToken' :'{{csrf_token}}',
        },
        body: JSON.stringyfy(ooota_kannadi)
    }).then(response =>{
        return response.json();
    }).then(data =>{
        alert(data['status']);

    });
    }
    else{
        alert("Please book yor ticket")
    }
});
