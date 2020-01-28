import * as React from 'react';
import { Text, View, StyleSheet, Image, TouchableOpacity } from 'react-native';
import ContentHeader from './comp/content_header';
import ContentFooter from './comp/content_footer';



export default class Imager extends React.Component {
  componentDidMount = () => {
    let url = '' + this.props.uuid + '/';
    fetch(url,
      {
      method:'get',
      header:{
        'Accept': 'application/json',
        'Content-Type': 'application/json'}
      }).then(res=>res.json()).then(res=>{func(res)})
  });

  constructor(props){
    super(props);
    this.state = {url:'',uuid:null}
    this.header = {proPic:'',uname:'',date:null}
    this.footer = {numLikes:0,numComs:0,liked:false,saved:false}
  }
  render() {
    return (

        <View style={{width:'100%',backgroundColor:'white', borderRadius:5}}>
          <ContentHeader PicLink={this.header.proPic} uname={this.header.uname} date={this.header.date} uuid={this.state.uuid}/>

            <TouchableOpacity style={{flex:1, padding:8}}>
              <Image style={{flex:1, borderRadius:10}} source={{ uri:{this.state.url} }}/>
            </TouchableOpacity>

            <ContentFooter numComs={this.footer.numComs} numLikes={this.footer.numLikes} liked={this.footer.liked} saved={this.footer.saved} uuid={this.state.uuid}/>
        </View>


    );
  }
}
