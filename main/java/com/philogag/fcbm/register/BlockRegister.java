package com.philogag.fcbm.register;

import jdk.nashorn.internal.ir.annotations.Reference;
import net.minecraft.block.Block;
import net.minecraft.client.renderer.block.model.ModelResourceLocation;
import net.minecraft.creativetab.CreativeTabs;
import net.minecraft.item.Item;
import net.minecraft.item.ItemBlock;
import net.minecraft.item.ItemStack;
import net.minecraftforge.client.event.ModelRegistryEvent;
import net.minecraftforge.client.model.ModelLoader;
import net.minecraftforge.event.RegistryEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.common.eventhandler.SubscribeEvent;

import java.util.ArrayList;
import java.util.Random;

@Mod.EventBusSubscriber
public class BlockRegister {

    // 待注册方块列表
    public static ArrayList<Block> BlockList = new ArrayList<>();

    // 新创造物品表
    public static final CreativeTabs tabBlock = new CreativeTabs("rgb_tab") {
        @Override
        public ItemStack getTabIconItem() {
            // 设置 标签
            Random r = new Random();
            return new ItemStack(BlockList.get(r.nextInt(BlockList.size())));
        }
    };

    public BlockRegister(){
        // 通过 MakeBlockList 类构造带待注册列表
        this.BlockList = new MakeBlockList().list;
    }

    // 注册方块
    @SubscribeEvent
    public static void registerBlocks(RegistryEvent.Register<Block> blocks){
        for(Block b: BlockList){
            blocks.getRegistry().registerAll(b);
        }
    }

    // 注册块物体
    @SubscribeEvent
    public static void registerItemBlocks(RegistryEvent.Register<Item> items){
        for(Block b : BlockList){
            items.getRegistry().registerAll(
                    new ItemBlock(b).setRegistryName(b.getRegistryName())
            );
        }
    }

    // 注册块手持模型
    @SubscribeEvent
    public static void registerRenders(ModelRegistryEvent event){
        for(Block b : BlockList){
            registerRender(Item.getItemFromBlock(b));
        }
    }

    public static void registerRender(Item item) {
        ModelLoader.setCustomModelResourceLocation(item, 0, new ModelResourceLocation( item.getRegistryName(), "inventory"));
    }
}