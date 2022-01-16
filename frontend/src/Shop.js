import React from 'react'
import './Home.css'
import Item from './item.js'

export default function Shop() {

    return (

        <div className = "row shop__container m-2">
            <div className='col-2 Shop__aside'>
                <ul>
                    <li>Catagories</li>
                </ul>
            </div>
            <div className='col-10 Shop__main'>
            <h1>Shop Name</h1>
            <p>The shop description comes here</p>

            <hr/>
            <div className = "Home__Row">
                
                <Item 
                Title = "Sony Camera" 
                rating={5}
                price={99.99}
                description='Sony Ultra hd Sony Camera for profesionals, used for many things high resolution 
                and unlimited storage 2021'
                
            />
                  
                <Item 
                Title = "Sony Camera" 
                rating={5}
                price={99.99}
                description='Sony Ultra hd Sony Camera for profesionals, used for many things high resolution 
                and unlimited storage 2021'
            />
                <Item 
                Title = "Sony Camera" 
                rating={5}
                price={99.99}
                description='Sony Ultra hd Sony Camera for profesionals, used for many things high resolution 
                and unlimited storage 2021'
                />
                <Item 
                Title = "Sony Camera" 
                rating={5}
                price={99.99}
                description='Sony Ultra hd Sony Camera for profesionals, used for many things high resolution 
                and unlimited storage 2021'
                />
                
            
                <Item />
                <Item />
                <Item 
                Title = "Sony Camera" 
                rating={5}
                price={99.99}
                description='Sony Ultra hd Sony Camera for profesionals, used for many things high resolution 
                and unlimited storage 2021'
                />
                <Item 
                Title = "Sony Camera" 
                rating={5}
                price={99.99}
                description='Sony Ultra hd Sony Camera for profesionals, used for many things high resolution 
                and unlimited storage 2021'
                />
             
                <Item />
                <Item />
                <Item 
                Title = "Sony Camera" 
                rating={5}
                price={99.99}
                description='Sony Ultra hd Sony Camera for profesionals, used for many things high resolution 
                and unlimited storage 2021'
                />
                <Item 
                Title = "Sony Camera" 
                rating={5}
                price={99.99}
                description='Sony Ultra hd Sony Camera for profesionals, used for many things high resolution 
                and unlimited storage 2021'
                />
            
            
                <Item 
                Title = "Sony Camera" 
                rating={5}
                price={99.99}
                description='Sony Ultra hd Sony Camera for profesionals, used for many things high resolution 
                and unlimited storage 2021'
                />
                <Item 
                Title = "Sony Camera" 
                rating={5}
                price={99.99}
                description='Sony Ultra hd Sony Camera for profesionals, used for many things high resolution 
                and unlimited storage 2021'
                />
                <Item 
                Title = "Sony Camera" 
                rating={5}
                price={99.99}
                description='Sony Ultra hd Sony Camera for profesionals, used for many things high resolution 
                and unlimited storage 2021'
                />
                <Item 
                Title = "Sony Camera" 
                rating={5}
                price={99.99}
                description='Sony Ultra hd Sony Camera for profesionals, used for many things high resolution 
                and unlimited storage 2021'
                />
                 <Item />
                
            </div>
            </div>
            
        </div>
    )
}
