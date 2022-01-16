import React from 'react'
import './item.css'
import './bootstrap.min.css'
import {Link} from "react-router-dom"

function Item({className, id, Title,price,image, rating, description}) {
   
    return (
        
        <div className={"item "+ className} >
        <img  src={require("./images/camera.jpeg")} alt={Title} className="card-img-top" />
        <div className="card-body">
            
            <h5 className="card-title">{Title}{Array(rating).fill().map((_,i)=>(<p> ⭐ </p>))}</h5>
            
            
            <p className="card-text"></p>
            <label>Price </label>
                 <small> $</small>
            <strong>{price}</strong>
        </div>
        
        <button> Add to Cart </button>    
       </div>
        
        
    )  
}

export default Item