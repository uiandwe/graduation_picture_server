import React from 'react';
import ReactDOM from 'react-dom';
import Carousel from './components/Carousel';

if (document.getElementById('Carousel')){
	const CarouselElement = document.getElementById('Carousel');
	ReactDOM.render(<Carousel />, CarouselElement);
}
