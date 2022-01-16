import React from 'react'
import Item from './item' 
import './Home.css'
import './bootstrap.min.css'
import Slider from './component/slider'




function Home() {
    return (
        <div>
             <Slider/>
        <div className="Home__Container">
        <h1>Popular Shops</h1>
        <div className = "Home__Row">
        
            
        </div>
        <h1>Find Shops by Catagory </h1> <a href='#'>See All </a>
        <div className = "Home__Row">
        
            
        </div>
    <h1>Trending Products</h1>
    <div className=''>
    <div className = "Home__Row">
            
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
        
    </div>
    
    </div>
        </div>
       
        
    )
}

export default Home