import * as React from 'react';
import { Text, View, StyleSheet,Button, TouchableOpacity, TextInput, ScrollView, Image,StatusBar, SafeAreaView, Picker, FlatList, Switch } from 'react-native';
import QPost from '../../content/QPostComp';
import displayDate from '../../app_funcs';


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

export default class HomeTabScreen extends React.Component {
  constructor(props){
    super(props);
    this.state = {};
    this.data;
  }

  APIAction = () => {
    fetch('http://127.0.0.1:8000/feed/profile',{method:'get',headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'Authorization': 'Token ' + TOKEN
    }}).then(res=>res.json()).then(res=>{
      if (res['outcome'] !== 'success'){
        console.log('error');
      } else {
        this.data=res.data;
        this.setState({});


      }
    })
  }

  componentDidMount(){
    console.log('profile')
  }


  render() {
    return (
      <SafeAreaView style={{flex:1,backgroundColor:'grey'}}>

        <FlatList
    data={this.data}
    keyExtractor={item => item.cuuid}
    ListHeaderComponent={
        <View style={{height:200,width:'100%', backgroundColor:'#ebebeb', justifyContent:'center',alignItems:'center'}}>
        <Text style={{fontSize:26,fontWeight:'700'}}>Profile Name</Text>
        <View style={{height:100,width:'100%', backgroundColor:'red', flexDirection:'row'}}>
        <View style={{flex:1}}>
        <Image style={{height:50, width:50, borderRadius:50/2}} source={{uri:'https://www.biography.com/.image/t_share/MTQyMDA0ODU4NTc5MzMwMTEx/kylie-jenner_gettyimages-602272520jpg.jpg'}}/></View>
        <View style={{flex:1}}>
        <Text>4oifn</Text>
        </View>
        </View>
        </View>
      }
    ItemSeparatorComponent = { FlatListItemSeparator }
    renderItem={({ item }) => {
    }}
        />


        <View style={{height:100,width:'100%', backgroundColor:'#ebebeb', justifyContent:'center',alignItems:'center'}}>
        <Text style={{fontSize:26,fontWeight:'700'}}>Bookmarks</Text>
        <View style={{height:50,width:'100%', backgroundColor:'red', flexDirection:'row'}}>
        <TouchableOpacity style={{flex:1,justifyContent:'center', alignItems:'center'}}><Text>Photos</Text></TouchableOpacity>
        <TouchableOpacity style={{flex:1,justifyContent:'center', alignItems:'center'}}><Text>Videos</Text></TouchableOpacity>
        <TouchableOpacity style={{flex:1,justifyContent:'center', alignItems:'center'}}><Text>QPosts</Text></TouchableOpacity>
        <TouchableOpacity style={{flex:1,justifyContent:'center', alignItems:'center'}}><Text>Posts</Text></TouchableOpacity>

        </View>
        </View>

        <View style={{height:150,width:'100%', backgroundColor:'#ebebeb', justifyContent:'center',alignItems:'center'}}>
        <Text style={{fontSize:26,fontWeight:'700'}}>Active Subs</Text>
        <View style={{height:70, backgroundColor:'red', width:'100%', flexDirection:'row'}}>
          <View style={{flex:1}}>
            <Image style={{height:50, width:50, borderRadius:50/2}} source={{uri:'https://www.biography.com/.image/t_share/MTQyMDA0ODU4NTc5MzMwMTEx/kylie-jenner_gettyimages-602272520jpg.jpg'}}/>
          </View>
          <View style={{flex:1, backgroundColor:'pink'}}>
            <Text>next payment</Text>
            <Text>cost</Text>
          </View>
          <View style={{flex:1, backgroundColor:'blue'}}>
            <Switch/>
            <Text>auto-renew</Text>
          </View>
        </View>

        </View>


        <View style={{height:50,width:'100%', backgroundColor:'#ebebeb', justifyContent:'center',alignItems:'center'}}>
        <Text style={{fontSize:26,fontWeight:'700'}}>Inactive Subs</Text>
        </View>

        <View style={{height:50,width:'100%', backgroundColor:'#ebebeb', justifyContent:'center',alignItems:'center'}}>
        <Text style={{fontSize:26,fontWeight:'700'}}>Card Info</Text>
        </View>


        <View style={{height:50,width:'100%', backgroundColor:'#ebebeb', justifyContent:'center',alignItems:'center'}}>
        <Text style={{fontSize:26,fontWeight:'700'}}>Notification App Settings</Text>
        </View>

        <View style={{height:150,width:'100%', backgroundColor:'#ebebeb', justifyContent:'center',alignItems:'center'}}>
          <Text style={{fontSize:26,fontWeight:'700'}}>Notification Email Settings</Text>
          <View style={{height:100,  backgroundColor:'red', width:'100%',}}>

            <View style={{width:'100%', height:40, backgroundColor:'green', flexDirection:'row', justifyContent:'space-between', alignItems:'center'}}>
              <Text>Notification Settings Name</Text>
              <Switch/>
            </View>

          </View>
        </View>

        <View style={{height:50,width:'100%', backgroundColor:'#ebebeb', justifyContent:'center',alignItems:'center'}}>
        <Text style={{fontSize:26,fontWeight:'700'}}>Become a creator</Text>
        </View>

      </SafeAreaView>
    );
  }
}



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
