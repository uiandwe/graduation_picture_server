import React from 'react';
import ReactDOM from 'react-dom'

const App = React.createClass({
    getInitialState : function(){
        return {
            auth : false
        }
    },

    componentDidMount: function() {
        console.log("!")
        $.get('/files/?type=shin').done(function(data) {
          this.setState({data: data});
        }.bind(this));
      },
  
    render(){
        console.log(this.state.data.data) 
        if (this.state.data) {
            var rows = [];


            for (var i=0; i < this.state.data.data.length; i++) {
                rows.push(
                <a >
                    <div className="album" >
                        <img src={this.state.data.data[i].path} className="img"/>
                        <div className="overlay">
                            <h3 className="title">starred</h3>
                            <a>0 photos</a>
                        </div>
                    </div>  
                </a>);
                
            }
          return <div>
                    {rows}
                 </div>;
        }
        
    }
});


export default App