
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
//import { createStackNavigator } from '@react-navigation/stack';

import Presentation from './pages/presentation';
import StartingSearch from './pages/startingSearch';
// import Register from './pages/register';
// import Points from './pages/points';
// import Detail from './pages/detail';
// import ReadyToGo from './pages/ready';
// import Maps from './pages/map';
// import Cupons from './pages/cupons';

const Drawer = createDrawerNavigator();

const Routes = () =>{
    return (
        <NavigationContainer independent={true}>
     <AppStack.Navigator 
                headerMode="none"
                screenOptions={{
                    cardStyle:{
                        backgroundColor:'#f0f0f5'
                    }
                }}
             >
                <AppStack.Screen name="Home" component={Home}/>
    </AppStack.Navigator> 
  

            <Drawer.Navigator initialRouteName="Home">
                <Drawer.Screen name="Presentation" component={Presentation} />
                <Drawer.Screen name="StartingSearch" component={StartingSearch} />
            </Drawer.Navigator>

        </NavigationContainer>
    )
}

export default Routes;