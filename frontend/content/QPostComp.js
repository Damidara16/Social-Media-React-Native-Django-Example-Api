import * as React from 'react';
import { Text, View, StyleSheet, Image, TouchableOpacity, Button } from 'react-native';
import ContentHeader from '../comp/content_header';
import ContentFooter from '../comp/h';
import displayDate from '../app_funcs';


export default class QPost extends React.Component {

  APIAction = () => {
    fetch('http://127.0.0.1:8000/content/detail/'+this.props.uuid+'/', {method:'get',headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'Authorization': 'Token 933d66153aec6d5b205eab69174300bd27ca415d'
    }}).then(res=>res.json()).then(res=>{
      if (res['outcome'] !== 'success'){
        console.log('error');
      } else {
        this.header = {uname:res.content_frame.uname, proPic:'http://wilmingtonbiz.s3.amazonaws.com/gwbj_0906_techmain.jpg', date:displayDate(res.content_frame.date)}
        this.footer = {numLikes:res.content_frame.numLikes, numComs:res.content_frame.numComs, liked:res.content_frame.liked, saved:res.content_frame.saved}
        this.setState({text:res.content_data.qpost,uuid:res.content_frame.uuid});
      }
    })
  }

  componentDidMount = () => {
    //console.log('qpost')
    this.APIAction()
  }

  constructor(props){
    super(props);
    this.state = {text:'',uuid:null}
    this.header = {picLink:'google.com',uname:'',date:''}
    this.footer = {numLikes:0,numComs:0,liked:false,saved:false}
  }
  render() {
    return (
      <View style={{flex:1,justifyContent:'center',alignItems:'center'}}>
        <View style={{width:'100%',backgroundColor:'white'}}>
          <ContentHeader PicLink={this.header.proPic} uname={this.header.uname} date={this.header.date} uuid={this.state.uuid}/>

          <View style={{height:100}}>
            <Text numberOfLines={5} style={{fontSize:14, paddingHorizontal:10, paddingTop:5}}>{this.state.text}</Text>
          </View>

          <ContentFooter numComs={this.footer.numComs} numLikes={this.footer.numLikes} liked={this.footer.liked} saved={this.footer.saved} uuid={this.state.uuid}/>
        </View>
        </View>
    );
  }
}
