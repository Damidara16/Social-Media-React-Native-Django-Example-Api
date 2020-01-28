import * as React from 'react';
import { Text, View, StyleSheet,Button, TouchableOpacity, TextInput, ScrollView, Image,StatusBar, SafeAreaView, Picker, FlatList } from 'react-native';
import QPost from '../../content/QPostComp';
import ContentHeader from '../../comp/content_header';
import ContentFooter from '../../comp/content_footer';
import displayDate from '../../app_funcs';
import AntDesign from 'react-native-vector-icons/AntDesign';
import MaterialCommunityIcons from 'react-native-vector-icons/MaterialCommunityIcons';
import Ionicon from 'react-native-vector-icons/Ionicons';
//import NFooter from '../../comp/content_nfooter'

const TOKEN = '933d66153aec6d5b205eab69174300bd27ca415d'

FlatListItemSeparator = () => {
  return (
    <View
      style={{
        height: 10
      }}
    ></View>
  );
}

export default class NotifTabScreen extends React.Component {
  constructor(props){
    super(props);
    this.state = {comment:false};
    this.data;
  }

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

  componentDidMount(){
    console.log('notif')
  }


  render() {
    const HEIGHT = 40;
    const COLOR = '#eeebeb';
    const BLOCK = 15;
    const IMGHEIGHT = [250,300,350,400,450]
    return (
          <TouchableOpacity style={{height:450, width:'95%'}}>
          <Image style={{height:'100%', width:'100%', overflow:'hidden',borderTopRightRadius:15, borderTopLeftRadius:15}} source={{uri:'https://www.destinsparks.com/wp-content/uploads/2017/03/tips-for-better-selfies.jpg'}}/>
          </TouchableOpacity>
          <ContentFooter c={true}/>


    );
  }
}


{/*
        <FlatList
    data={this.data}
    keyExtractor={item => item.cuuid}
    ListHeaderComponent={
        <View style={{height:50,width:'100%', backgroundColor:'#ebebeb', justifyContent:'center',alignItems:'center'}}>
        <Text style={{fontSize:26,fontWeight:'700'}}>Notifications</Text>
        </View>
      }
    ItemSeparatorComponent = { FlatListItemSeparator }
    renderItem={({ item }) => {
      switch (item.type) {
       case 'post':
         return <Poster uuid={item.cuuid}/>
         break;
       case 'qpost':
         return <QPost uuid={item.cuuid}/>
         break;
       case 'image':
          return <Imager uuid={item.cuuid}/>

         break;


     }}}


        />*/}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: 10,
  },
  item: {
    backgroundColor: '#f9c2ff',
    padding: 20,
    marginVertical: 8,
    marginHorizontal: 16,
  },
  title: {
    fontSize: 32,
  },
});
