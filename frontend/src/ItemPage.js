import React from 'react'
import { Link } from 'react-router-dom'
import './bootstrap.min.css'
import Item from './item'
import './itempage.css'
import Review from './Review'

export default function ItemPage(Title , description, Rating, Images) {
    return (

        <div className='Container p-5 row'>
        <div className='col-md-5 item-photos'>
            <img className='img-fluid' src={require("./images/camera.jpeg")}/>
            <div className='images row'>
            <img className='img-thumbnail' src={require("./images/camera.jpeg")}/>
            <img className='img-thumbnail' src={require("./images/camera.jpeg")}/>
            <img className='img-thumbnail' src={require("./images/camera.jpeg")}/>
            <img className='img-thumbnail' src={require("./images/camera.jpeg")}/>
            <img className='img-thumbnail' src={require("./images/camera.jpeg")}/>
            </div>
        </div> 
        
        <div className="col-md-7">
        <h3 class="product-name">Camera</h3>
		<h4 class="product-price">Price $980.00 <del class="product-old-price">$990.00</del></h4>
        <h4 className='d-flex'>{Array(4).fill().map((_,i)=>(<p> ⭐ </p>))} <small>&nbsp; 44,000</small></h4>
        <p>
         Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </p>
        <ul class="list-group">
        <li class="list-group-item">Ram - 5gb</li>
        <li class="list-group-item">Resolution - 8080px</li>
        <li class="list-group-item">New </li>
        <li class="list-group-item">5050hhd</li>
        <li class="list-group-item">Clear Vision</li>
        </ul>
        <div className='mt-2 '>
        <Link to={'/review'}>Give Review and Rate it Your self!</Link>

        </div>
        
        <button className='btn btn-primary mt-2'>Add to Cart</button>
		</div>
        
        <div className='Container'>
         <h2 >Related Products</h2>
         <div className='row'>
                <Item className='w-10' 
                Title = "Hd Camera" 
                rating={5}
                price={99.99}
                />
                <Item className='w-10' 
                Title = "Camera" 
                rating={5}
                price={99.99}
                />
                <Item className='w-10' 
                Title = "Camera" 
                rating={5}
                price={99.99}
                />
                <Item className='w-10' 
                Title = "Camera" 
                rating={5}
                price={99.99}
                />
         </div>

         <h3 className='m-3'>Top Reviews</h3>
         <div>
             <Review/>
             <Review/>
             <Review/>
         </div>


        </div>
        </div>
    )
}
