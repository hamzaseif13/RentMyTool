const daysInput = document.getElementById('id_rental_days')
if (daysInput){
    daysInput.addEventListener('change',(event)=>{
        let price = parseInt(document.getElementById('price').innerText.slice(1))
        document.getElementById('totalprice').innerText=price*event.target.value

    })
}