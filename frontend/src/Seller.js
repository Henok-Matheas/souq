import React from 'react'
import './Home.css'
import Item from './item.js'
import Shop from './Shop.js'

export default function Seller() {

    return (

        <div className = "row shop__container m-2">
            <div className='col-2 '>
                <div className='card'>

                </div>
            </div>
            <div className='col-10 Shop__main'>
            <h1>Shop Name</h1>
            <p>Lorem ipsum dolor esoma sisi lavada simi vo la shipata every where</p>

            <hr/>
            <div className = "Home__Row">
                
                <Item 
                Title = "learn React" 
                rating={5}
                price={99.99}   
            />
                  
                <Item 
                Title = "learn React" 
                rating={5}
                price={99.99}
            />
                <Item 
                Title = "learn React" 
                rating={5}
                price={99.99}
                />
                <Item 
                Title = "learn React" 
                rating={5}
                price={99.99}
                />
                
            
                <Item />
                <Item />
                <Item 
                Title = "learn React" 
                rating={5}
                price={99.99}
                />
                <Item 
                Title = "learn React" 
                rating={5}
                price={99.99}
                />
             
                <Item />
                <Item />
                <Item 
                Title = "learn React" 
                rating={5}
                price={99.99}
                />
                <Item 
                Title = "learn React" 
                rating={5}
                price={99.99}
                />
            
            
                <Item 
                Title = "learn React" 
                rating={5}
                price={99.99}
                />
                <Item 
                Title = "learn React" 
                rating={5}
                price={99.99}
                />
                <Item 
                Title = "learn React" 
                rating={5}
                price={99.99}
                />
                <Item 
                Title = "learn React" 
                rating={5}
                price={99.99}
                />
                
            </div>
            </div>
            
        </div>
    )
}