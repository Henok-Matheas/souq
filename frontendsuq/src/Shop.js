import React from 'react'
import './Home.css'
import Item from './item.js'

export default function Shop({id, Name,Location,Logo, Rating, description}) {

    return (

        <div className = "row shop__container m-2">
            <div className='col-2 Shop__aside'>
                <ul>
                    <li>Catagories</li>
                </ul>
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
                 <Item />
                
            </div>
            </div>
            
        </div>
    )
}
