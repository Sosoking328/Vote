package com.sosokan.android.control.multi.level.menu;

/**
 * Created by AnhZin on 10/3/2016.
 */


import java.util.List;

/**
 * Class used to represent MultiLevelListView items. User objects are wrapped with this type.
 */
public class Node {

    private Object mObject;
    private int mLevel;
    private Node mParent;
    private List<Node> mSubNodes;
    private int mIdxInLevel;
    private int mLevelSize;
    private boolean mIsExpandable;
    private NodeItemInfo mNodeItemInfo;

    public String getCategorySelectedId() {
        return categorySelectedId;
    }

    public void setCategorySelectedId(String categorySelectedId) {
        this.categorySelectedId = categorySelectedId;
    }

    private String categorySelectedId;


    private boolean mIsSelected;
    /**
     * Constructor.
     *
     * @param object Wrapped object.
     * @param parent Wrapped object parent. Null is possible.
     */
    Node(Object object, Node parent) {
        mObject = object;
        mParent = parent;
        mLevel = parent.mLevel + 1;
    }

    /**
     * Constructor.
     */
    Node() {
        mLevel = -1;
    }

    /**
     * Gets node wrapped object.
     *
     * @return Wrapped object.
     */
    public Object getObject() {
        return mObject;
    }

    /**
     * Gets node level. Levels starts from 0.
     *
     * @return Node level.
     */
    int getLevel() {
        return mLevel;
    }

    /**
     * Gets node parent. Null is possible.
     *
     * @return Node parent.
     */
    Node getParent() {
        return mParent;
    }

    /**
     * Clears node sub-nodes (childs).
     */
    void clearSubNodes() {
        mSubNodes = null;
    }

    /**
     * Sets node sub-nodes (childs).
     *
     * @param nodes List of sub-nodes.
     */
    void setSubNodes(List<Node> nodes) {
        mSubNodes = nodes;

        final int NODES = nodes.size();
        for (int i = 0; i < NODES; ++i) {
            Node node = nodes.get(i);
            node.mLevelSize = NODES;
            node.mIdxInLevel = i;
        }
    }

    /**
     * Gets info if node is expanded.
     *
     * @return true if node is expanded, false otherwise.
     */
    boolean isExpanded() {
        return mSubNodes != null;
    }
    /**
     * Gets node index within its level.
     *
     * @return Node index within its level.
     */
    int getIdxInLevel() {
        return mIdxInLevel;
    }

    /**
     * Gets level size.
     *
     * @return Level size.
     */
    int getLevelSize() {
        return mLevelSize;
    }

    /**
     * Gets node sub-nodes (childs).
     *
     * @return Node sub-nodes (childs).
     */
    List<Node> getSubNodes() {
        return mSubNodes;
    }

    /**
     * Get node info.
     *
     * @return Node info.
     */
    NodeItemInfo getItemInfo() {
        if (mNodeItemInfo == null) {
            mNodeItemInfo = new NodeItemInfo(this);
        }
        return mNodeItemInfo;
    }

    /**
     * Sets whether node is expandable or not.
     *
     * @param isExpandable node expandable value.
     */
    void setExpandable(boolean isExpandable) {
        mIsExpandable = isExpandable;
    }
    void setSelected(boolean isSelected) {
        mIsSelected = isSelected;
    }

    /**
     * Indicates if node is expandable.
     *
     * @return true if object is expandable, false otherwise.
     */
    boolean isExpandable() {
        return mIsExpandable;
    }
    boolean isSelected() {
        return mIsSelected;
    }
}