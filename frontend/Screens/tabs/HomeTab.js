import * as React from 'react';
import { Text, View, StyleSheet,Button, TouchableOpacity, TextInput, ScrollView, Image,StatusBar, SafeAreaView, Picker, FlatList } from 'react-native';
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
    fetch('http://127.0.0.1:8000/feed/home/',{method:'get',headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'Authorization': 'Token ' + TOKEN
    }}).then(res=>res.json()).then(res=>{
      if (res['outcome'] !== 'success'){
        console.log('error');
      } else {
        this.data=res.data;
        this.setState({});
        console.log(this.data)
        //this.forceUpdate();

      }
    })
  }

  componentDidMount(){
    this.APIAction();
    console.log('feed1')
  }


  render() {
    return (
      <SafeAreaView style={{flex:1,backgroundColor:'grey'}}>

        <FlatList
    data={this.data}
    keyExtractor={item => item.cuuid}
    ListHeaderComponent={
        <View style={{height:50,width:'100%', backgroundColor:'#ebebeb', justifyContent:'center',alignItems:'center'}}>
        <Text style={{fontSize:26,fontWeight:'700'}}>FanMojis</Text>
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
        />

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
