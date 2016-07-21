import React from 'react';
import ReactDOM from 'react-dom'

const Carousel = React.createClass({
    getInitialState : function(){
        return {
            auth : false
        }
    },

    componentDidMount: function() {
        var type = getUrlParameter('type');
        $.get('http://127.0.0.1:8000/files/?type='+type).done(function(data) {
          this.setState({data: data});
        }.bind(this));
      },
  
    render(){
        if (this.state.data) {
            var rows = [];

            for (var i=0; i < this.state.data.data.length; i++) {
                if( i == 0){
                    var active = 'active';
                    rows.push(<img src={this.state.data.data[i].path} className="active" />);
                }
                else{
                    rows.push(<img src={this.state.data.data[i].path}/>);    
                }
                
            }
          return <div>
                    {rows}
                 </div>;
        }
        
        return <div></div>
        
    }
});


var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};


export default Carousel