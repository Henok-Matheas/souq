import React from 'react'
import './review.css'

function Review() {
    return (
        <div>
         <div class="card-head"> <h6><img className='rounded-circle' src={require('./images/head.jpeg')} /> Name</h6></div>
        <div class="card text-dark bg-light mb-3 review">
        <div class="card-body">
            <p class="card-text">it is aa great camera i like it, been taking photos for weeks and 
            the quilty is unbeliveable thank you</p>
        </div>
        </div>
        </div>
    
    )
}


export default Review
